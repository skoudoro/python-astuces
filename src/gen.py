"""Convert markdown to html and send it to SendinBlue."""
import os
import re
import json
from datetime import datetime, timezone
from email import utils
import markdown as md
import jinja2
import click
import sib_api_v3_sdk
from sib_api_v3_sdk.rest import ApiException

CODE_STYLE = """
.codehilite .hll { background-color: #49483e }
.codehilite  { background: #f8f8f8; overflow:auto;width:auto;border:solid gray;border-width:.1em .1em .1em .8em;padding:.2em .6em; }
.codehilite .c { color: #008800 } /* Comment */
.codehilite .err { color: #960050; background-color: #1e0010 } /* Error */
.codehilite .k { color: #aa22ff } /* Keyword */
.codehilite .l { color: #ae81ff } /* Literal */
.codehilite .n { color: #272822 } /* Name */
.codehilite .o { color: #f92672 } /* Operator */
.codehilite .p { color: #272822 } /* Punctuation */
.codehilite .ch { color: #008800 } /* Comment.Hashbang */
.codehilite .cm { color: #008800 } /* Comment.Multiline */
.codehilite .cp { color: #008800 } /* Comment.Preproc */
.codehilite .cpf { color: #008800 } /* Comment.PreprocFile */
.codehilite .c1 { color: #008800 } /* Comment.Single */
.codehilite .cs { color: #008800 } /* Comment.Special */
.codehilite .gd { color: #f92672 } /* Generic.Deleted */
.codehilite .ge { font-style: italic } /* Generic.Emph */
.codehilite .gi { color: #a6e22e } /* Generic.Inserted */
.codehilite .go { color: #aa22ff } /* Generic.Output */
.codehilite .gp { color: #f92672; font-weight: bold } /* Generic.Prompt */
.codehilite .gs { font-weight: bold } /* Generic.Strong */
.codehilite .gu { color: #75715e } /* Generic.Subheading */
.codehilite .kc { color: #aa22ff } /* Keyword.Constant */
.codehilite .kd { color: #aa22ff } /* Keyword.Declaration */
.codehilite .kn { color: #f92672 } /* Keyword.Namespace */
.codehilite .kp { color: #aa22ff } /* Keyword.Pseudo */
.codehilite .kr { color: #aa22ff } /* Keyword.Reserved */
.codehilite .kt { color: #aa22ff } /* Keyword.Type */
.codehilite .ld { color: #e6db74 } /* Literal.Date */
.codehilite .m { color: #ae81ff } /* Literal.Number */
.codehilite .s { color: #e6db74 } /* Literal.String */
.codehilite .na { color: #0000ff } /* Name.Attribute */
.codehilite .nb { color: #272822 } /* Name.Builtin */
.codehilite .nc { color: #0000ff } /* Name.Class */
.codehilite .no { color: #aa22ff } /* Name.Constant */
.codehilite .nd { color: #0000ff } /* Name.Decorator */
.codehilite .ni { color: #272822 } /* Name.Entity */
.codehilite .ne { color: #0000ff } /* Name.Exception */
.codehilite .nf { color: #0000ff } /* Name.Function */
.codehilite .nl { color: #272822 } /* Name.Label */
.codehilite .nn { color: #272822 } /* Name.Namespace */
.codehilite .nx { color: #0000ff } /* Name.Other */
.codehilite .py { color: #272822 } /* Name.Property */
.codehilite .nt { color: #f92672 } /* Name.Tag */
.codehilite .nv { color: #272822 } /* Name.Variable */
.codehilite .ow { color: #f92672 } /* Operator.Word */
.codehilite .w { color: #272822 } /* Text.Whitespace */
.codehilite .mb { color: #ae81ff } /* Literal.Number.Bin */
.codehilite .mf { color: #ae81ff } /* Literal.Number.Float */
.codehilite .mh { color: #ae81ff } /* Literal.Number.Hex */
.codehilite .mi { color: #ae81ff } /* Literal.Number.Integer */
.codehilite .mo { color: #ae81ff } /* Literal.Number.Oct */
.codehilite .sa { color: #0066bb } /* Literal.String.Affix */
.codehilite .sb { color: #0066bb } /* Literal.String.Backtick */
.codehilite .sc { color: #0066bb } /* Literal.String.Char */
.codehilite .dl { color: #0066bb } /* Literal.String.Delimiter */
.codehilite .sd { color: #0066bb } /* Literal.String.Doc */
.codehilite .s2 { color: #0066bb } /* Literal.String.Double */
.codehilite .se { color: #ae81ff } /* Literal.String.Escape */
.codehilite .sh { color: #0066bb } /* Literal.String.Heredoc */
.codehilite .si { color: #0066bb } /* Literal.String.Interpol */
.codehilite .sx { color: #0066bb } /* Literal.String.Other */
.codehilite .sr { color: #0066bb } /* Literal.String.Regex */
.codehilite .s1 { color: #0066bb } /* Literal.String.Single */
.codehilite .ss { color: #0066bb } /* Literal.String.Symbol */
.codehilite .bp { color: #272822 } /* Name.Builtin.Pseudo */
.codehilite .fm { color: #0000ff } /* Name.Function.Magic */
.codehilite .vc { color: #272822 } /* Name.Variable.Class */
.codehilite .vg { color: #272822 } /* Name.Variable.Global */
.codehilite .vi { color: #272822 } /* Name.Variable.Instance */
.codehilite .vm { color: #272822 } /* Name.Variable.Magic */
.codehilite .il { color: #ae81ff } /* Literal.Number.Integer.Long */
"""

RSS_TEMPLATE = """
<item>
    <title>Python Astuces #{{numero}} - {{title}}</title>
    <link>https://pythonastuces.com/archives/numero-{{numero}}</link>
    <guid>https://pythonastuces.com/archives/numero-{{numero}}</guid>
    <pubDate>{{date}}</pubDate>
</item>

"""

TEMPLATE = """<!DOCTYPE html>
<html lang="fr">
<head>
    <title>Python Astuces, Newsletter Python</title>
    <meta charset="UTF-8">
    <meta name="description" content="Recevez chaque semaines des astuces Python dans votre email">
    <meta name="keywords" content="newsletter, newsletters, python, python3, astuces, email">
    <meta name="author" content="Python Astuces (info@pythonastuces.com)">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="robots" content="index,follow" />
    <meta property="og:locale" content="fr_FR" />
    <meta property="og:type" content="website" />
    <meta property="og:title" content="Python Astuces : Newsletter hebdomadaire fournissant un code snippet python" />
    <meta property="og:description" content="Python Astuces, publié chaque dimanche, est une newsletter hebdomadaire vous permettant d'améliorer vos compétences Python à travers des astuces." />
    <meta property="og:url" content="https://pythonastuces.com" />
    <meta property="og:site_name" content="Python Astuces : Recevez chaque semaines des astuces Python dans votre email" />
    <meta property="og:image" content="https://pythonastuces.com/images/preview.png">
    <meta property="og:image:secure_url" content="https://pythonastuces.com/images/preview.png" />
    <meta name="twitter:card" content="summary_large_image" />
    <meta name="twitter:description" content="Python Astuces, publié chaque dimanche, est une newsletter hebdomadaire vous permettant d'améliorer vos compétences Python à travers des astuces." />
    <meta name="twitter:title" content="Python Astuces : Recevez chaque semaines des astuces Python dans votre email" />
    <meta name="twitter:site" content="@pythonastuces" />
    <meta name="twitter:image" content="https://pythonastuces.com/images/preview.png" />
    <meta name="twitter:image:secure_url" content="https://pythonastuces.com/images/preview.png" />
    <meta name="twitter:image:alt" content="Python Astuces - logo" />
    <meta name="twitter:creator" content="@skoudoro" />
    <link rel="canonical" href="https://pythonastuces.com/" />
<!--===============================================================================================-->
    <link rel="icon" type="image/png" href="images/icons/favicon.ico"/>
<!--===============================================================================================-->
    <link rel="stylesheet" type="text/css" href="vendor/bootstrap/css/bootstrap.min.css">
<!--===============================================================================================-->
    <link rel="stylesheet" type="text/css" href="fonts/font-awesome-4.7.0/css/font-awesome.min.css">
<!--===============================================================================================-->
    <link rel="stylesheet" type="text/css" href="vendor/animate/animate.css">
<!--===============================================================================================-->
    <link rel="stylesheet" type="text/css" href="../css/util.css">
    <link rel="stylesheet" type="text/css" href="../css/main.css">
<!--===============================================================================================-->
<style type="text/css" media="screen">
{{pycodestyle}}
img{
    width : 30px;
}
h1 {
    font-size : 30px;
}
h4 {
      padding : 20px
    }
p {
    margin : 14px;
}
blockquote {
  border-left: 5px solid #ccc;
  margin: 1.5em 20px;
  font-style: italic;
  }
</style>
</head>
<body>
<div class="size1 overlay2 bg-img-code where1-parent">
<div class="bgwhite size3 m-lr-auto p-l-75 p-r-75 p-t-35 p-b-25">
{{content}}
</div>
</div>
<!--===============================================================================================-->
    <script src="vendor/jquery/jquery-3.2.1.min.js"></script>
<!--===============================================================================================-->
    <script src="vendor/bootstrap/js/popper.js"></script>
    <script src="vendor/bootstrap/js/bootstrap.min.js"></script>
<!--===============================================================================================-->
    <script src="js/main.js"></script>
<!--===============================================================================================-->
    <!-- Global site tag (gtag.js) - Google Analytics -->
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-3RV5DTCLJJ"></script>
    <script>
        window.dataLayer = window.dataLayer || [];
        function gtag(){dataLayer.push(arguments);}
        gtag('js', new Date());

        gtag('config', 'G-3RV5DTCLJJ');
    </script>
<!--===============================================================================================-->

</body>
</html>
"""


def get_script_path():
    """Return script path folder."""
    return os.path.dirname(os.path.realpath(__file__))


def extract_from_tag(text, start, end):
    """Extract a substring from a tag.

    Parameters
    ----------
    text : str
        full text
    start : str
        starting string
    end : str
        end string
    """
    try:
        found = re.search('{}(.+?){}'.format(start, end), text).group(1)
    except AttributeError:
        found = ''

    return found


def convert_to_html(filename):
    """Convert Markdown file to html.

    Parameters
    ----------
    filename : str
        markdown filename

    """
    with open(filename, 'r') as f:
        data = f.read()

    title = extract_from_tag(data, '<!--title:', '-->').strip()

    extensions = ['extra', 'codehilite', 'smarty']
    md_txt = md.markdown(data, extensions=extensions,
                         output_format='html5')
    # print(md_txt)
    return md_txt, title


def create_rss_file(fname):
    """Create a default rss file.

    Parameters
    ----------
    fname : str
        rss file name

    """
    DEFAULT_RSS_TEMPLATE = """<?xml version="1.0" encoding="utf-8"?>
<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom">
<channel>
   <title>Python Astuces - archives</title>
   <description>Python Astuces - archives</description>
   <link>https://pythonastuces.com</link>
   <atom:link href="https://pythonastuces.com/rss.xml"
     rel="self" type="application/rss+xml" />
</channel>
</rss>
"""
    with open(fname, 'w') as f:
        f.write(DEFAULT_RSS_TEMPLATE)


def update_rss(rss_file, numero_id, title=''):
    """Update rss file.

    Parameters
    ----------
    rss_file : str
        rss file name
    numero_id : int
        numero of the episode
    title : str

    """
    text_to_replace = 'type="application/rss+xml" />'
    with open(rss_file, 'r') as f:
        rss_data = f.read()

    now = datetime.now(timezone.utc)
    now_str = utils.format_datetime(now)
    rss_item = jinja2.Template(RSS_TEMPLATE).render(numero=numero_id,
                                                    date=now_str, title=title)
    rss_data = rss_data.replace(text_to_replace,
                                "{}\n{}".format(text_to_replace, rss_item))
    with open(rss_file, 'w') as f:
        f.write(rss_data)


def update_archives_list(numero_id, title):
    """Update archives list.

    Parameters
    ----------
    numero_id : int
        [description]
    title : str
        [description]
    """
    folder = get_script_path()
    fname = os.path.join(folder, '..', 'archives.html')
    with open(fname, 'r') as f:
        txt = f.read()
    txt_to_replace = '<!--new_archive_to_add-->'
    li_tag = '<li class= "p-b-10">'
    li_tag += '<a href="archives/numero-{}.html">'.format(numero_id)
    li_tag += '#{} - {}</a></li>'.format(numero_id, title)
    txt = txt.replace(txt_to_replace,
                      '{}\n\t\t\t\t{}'.format(li_tag, txt_to_replace))
    with open(fname, 'w') as f:
        f.write(txt)


def upload_to_sib(content, numero_id, title, hours="18:00:00"):
    folder = get_script_path()
    fname = os.path.join(folder, 'sib.keys')
    if not os.path.isfile(fname):
        raise IOError("Please, create configuration file for upload")

    with open(fname, 'r') as f:
        config_data = json.load(f)
    configuration = sib_api_v3_sdk.Configuration()
    configuration.api_key['api-key'] = config_data.get('api-key-v3')

    api_client = sib_api_v3_sdk.ApiClient(configuration)
    api_instance = sib_api_v3_sdk.AccountApi(api_client)

    try:
        # Get your account informations, plans and credits details
        api_response = api_instance.get_account()
        print(api_response)
    except ApiException as e:
        print("Exception when calling AccountApi->get_account: %s\n" % e)

    # now = datetime.now(timezone.utc)
    # scheduled_at = now.strftime("%Y-%m-%dT{}Z".format(hours))
    api_instance = sib_api_v3_sdk.EmailCampaignsApi(api_client)

    # Define the campaign settings\
    email_campaigns = sib_api_v3_sdk.CreateEmailCampaign(
        name="Python Astuces #{}".format(numero_id),
        subject="Python Astuces #{} - {}".format(numero_id, title),
        sender={"name": "Python Astuces", "email": "info@pythonastuces.com"},
        reply_to="info@pythonastuces.com",
        html_content=content,
        # Select the recipients\
        recipients={"listIds": [2, ]},
        # scheduled_at=scheduled_at,
        # inline_image_activation=True
        )

    # Make the call to the client\
    try:
        api_response = api_instance.create_email_campaign(email_campaigns)
        print(api_response)
    except ApiException as e:
        msg = "Exception when calling"
        msg += " EmailCampaignsApi->create_email_campaign:%s\n" % e
        print(msg)


@click.command()
@click.option('--with_rss', is_flag=True,
              help='Update rss with the current numero')
@click.option('--with_archive_list', is_flag=True,
              help='Update archives list with the current numero')
@click.option('--upload_sib', is_flag=True,
              help='Upload html to SendinBlue')
@click.argument('numero_id')
def main(numero_id=None, with_rss=False, with_archive_list=False,
         upload_sib=False):
    """Convert markdown to html and update the newsletter to all platform.

    e.g : python gen.py 01 --with_rss --with_archive_list --upload_sib

    Parameters
    ----------
    numero_id : int
        newsletter version number to grab, by default None
    with_rss : bool, optional
        update rss feed with the new edition, by default False
    with_archive_list : bool, optional
        update archives.html file with the new edition, by default False
    upload_sib : bool, optional
        create email template and schedule it via sendinblue, by default False

    """
    folder = get_script_path()
    fname = "numero-{}.md".format(numero_id)
    fname = os.path.join(folder, fname)
    out_fname = "numero-{}.html".format(numero_id)
    out_fname = os.path.join(folder, "..", "archives", out_fname)
    html, title = convert_to_html(fname)
    doc = jinja2.Template(TEMPLATE).render(content=html,
                                           pycodestyle=CODE_STYLE)
    with open(out_fname, 'w') as f:
        f.write(doc)

    if with_rss:
        rss_file = os.path.join(folder, "..", "rss.xml")
        if not os.path.isfile(rss_file):
            create_rss_file(rss_file)
        update_rss(rss_file, numero_id, title)

    if with_archive_list:
        update_archives_list(numero_id, title)

    if upload_sib:
        upload_to_sib(doc, numero_id, title)


if __name__ == '__main__':
    main()

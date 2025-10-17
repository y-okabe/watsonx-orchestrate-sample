import smtplib
from ibm_watsonx_orchestrate.agent_builder.tools import tool
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

@tool
def send_gmail(to: str, subject: str, body: str) -> str:
    """
    指定した宛先にGmailを送信します。

    :param to: 送信先メールアドレス
    :param subject: メールの件名
    :param body: メール本文
    :return: 成功またはエラーのメッセージ
    """

    # Gmailアカウント情報
    gmail_user = 'あなたのメールアドレス'
    gmail_password = 'パスワード'

    # メール内容
    msg = MIMEMultipart()
    msg['From'] = gmail_user
    msg['To'] = to
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(gmail_user, gmail_password)
            server.send_message(msg)
        return 'メールを送信しました'
    except Exception as e:
        return 'エラーが発生しました: ' + str(e)

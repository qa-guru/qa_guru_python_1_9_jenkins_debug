import allure
from allure_commons.types import AttachmentType


class Attach:
    def add_png(self, browser):
        png = browser.driver.get_screenshot_as_png()
        allure.attach(body=png, name='screenshot', attachment_type=AttachmentType.PNG, extension='.png')

    def add_video(self, browser):
        video_url = "https://selenoid.autotests.cloud/video/" + browser.driver.session_id + ".mp4"
        html = "<html><body><video width='100%' height='100%' controls autoplay><source src='" \
               + video_url \
               + "' type='video/mp4'></video></body></html>"
        allure.attach(body=html, name='video', attachment_type=AttachmentType.HTML, extension='.html')

    def add_logs(self, browser):
        """log_type of browser logs should be equal to log_type in DesiredCapabilities."""
        logs = "".join(f'{text}\n' for text in browser.driver.get_log(log_type='browser'))
        allure.attach(body=logs, name='browser_logs', attachment_type=AttachmentType.TEXT, extension='.log')

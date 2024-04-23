# coding=utf-8
import os
import subprocess
import shlex

from core import HackingTool
from core import HackingToolsCollection

class HatCloud(HackingTool):
    TITLE = "HatCloud - Bypass CloudFlare to discover real IP"
    DESCRIPTION = "HatCloud, built in Ruby, bypasses CloudFlare to discover the real IP of a server."
    INSTALL_COMMANDS = ["git clone https://github.com/HatBashBR/HatCloud.git"]
    PROJECT_URL = "https://github.com/HatBashBR/HatCloud"

    def run(self):
        site = input("Enter Site >> ").strip()
        try:
            if not os.path.exists("HatCloud"):
                print("HatCloud directory not found. Please install it using the provided commands.")
                return
            os.chdir("HatCloud")
            subprocess.run(["sudo", "ruby", "hatcloud.rb", "-b", shlex.quote(site)], check=True)
        except FileNotFoundError:
            print("Ruby or HatCloud is not installed. Please check your installation.")
        except subprocess.CalledProcessError as e:
            print(f"Error executing HatCloud: {e}")
        finally:
            os.chdir("..")  # Return to the original directory

class OtherTools(HackingToolsCollection):
    TITLE = "Other tools"
    TOOLS = [
        HatCloud(),
        SocialMediaFinderTools(),
        WebCrawlingTools(),
    ]

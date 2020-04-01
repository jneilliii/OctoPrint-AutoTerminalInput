# coding=utf-8
from __future__ import absolute_import

import octoprint.plugin

class AutoterminalinputPlugin(octoprint.plugin.AssetPlugin,octoprint.plugin.ReloadNeedingPlugin):

	##~~ AssetPlugin mixin

	def get_assets(self):
		return dict(
			js=["js/AutoTerminalInput.js"]
		)

	##~~ Softwareupdate hook

	def get_update_information(self):
		return dict(
			AutoTerminalInput=dict(
				displayName="Autoterminalinput Plugin",
				displayVersion=self._plugin_version,

				# version check: github repository
				type="github_release",
				user="jneilliii",
				repo="OctoPrint-AutoTerminalInput",
				current=self._plugin_version,

				# update method: pip
				pip="https://github.com/jneilliii/OctoPrint-AutoTerminalInput/archive/{target_version}.zip"
			)
		)


__plugin_name__ = "Auto Terminal Input"
__plugin_pythoncompat__ = ">=2.7,<4"

def __plugin_load__():
	global __plugin_implementation__
	__plugin_implementation__ = AutoterminalinputPlugin()

	global __plugin_hooks__
	__plugin_hooks__ = {
		"octoprint.plugin.softwareupdate.check_config": __plugin_implementation__.get_update_information
	}


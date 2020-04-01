/*
 * View model for OctoPrint-AutoTerminalInput
 *
 * Author: jneilliii
 * License: AGPLv3
 */
$(function() {
	function AutoterminalinputViewModel(parameters) {
		var self = this;

		self.onAfterTabChange = function (current, previous) {
			if (current === "#term") {
				setTimeout(function(){$('#terminal-command').focus();},500);
			}
			return;
		};
	}

	OCTOPRINT_VIEWMODELS.push({
		construct: AutoterminalinputViewModel,
		dependencies: [],
		elements: []
	});
});

# -*- coding: utf-8 -*-
# Copyright (c) 2018 SubDownloader Developers - See COPYING - GPLv3

from subdownloader.client.state import BaseState, SubtitlePathStrategy


class CliState(BaseState):
    def __init__(self, options):
        BaseState.__init__(self, options=options, settings=None)
        self._options = options

        self._interactive = self._options.program.client.cli.interactive
        self._recursive = self._options.search.recursive

        self._cli_load_state()

        self.set_subtitle_rename_strategy(options.download.rename_strategy)
        self.set_subtitle_download_path_strategy(SubtitlePathStrategy.SAME)

        # FIXME: log state

    @property
    def interactive(self):
        return self._interactive

    @property
    def recursive(self):
        return self._recursive

    @recursive.setter
    def recursive(self, recursive):
        self._recursive = recursive

    def _cli_load_state(self):
        pass

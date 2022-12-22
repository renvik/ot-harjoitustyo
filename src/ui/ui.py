from services.train_service import TrainService
from ui.search_view import SearchView
from ui.results_view import ResultsView

class UI:
    """Class responsible for the ui"""
    def __init__(self, root): 
        """the constructor for the class, instantiates a new UI-object
        Args:
            root:
            TKinter-element into which the user interface is initialized
        """
        self._root = root
        self.train_service = TrainService()
        self._current_view = None

    def start(self):
        """Renders the ui"""
        self._show_search_view()

    def _hide_current_view(self):
        if self._current_view:
            self._current_view.destroy()

        self._current_view = None

    def _show_search_view(self):
        self._hide_current_view()

        self._current_view = SearchView(
            self._root, self._show_results_view
        )
        self._current_view.pack()

    def _show_results_view(self, results):
        self._hide_current_view()

        self._current_view = ResultsView(self._root,
            self._show_search_view)

        self._current_view.pack()
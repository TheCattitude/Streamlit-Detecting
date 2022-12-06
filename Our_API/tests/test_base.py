"""
Tests base class
"""

import inspect
import pickle
import os


def write_result(name, subdir=None, **kwargs):
    """
    saves the parameters into pickle files
    """

    # build pickle filename
    filename = os.path.join(
        os.path.dirname(__file__),
        subdir if subdir is not None else "",
        f"{name}.pickle")

    # save results
    with open(filename, "wb") as file:
        pickle.dump(kwargs, file)


class TestBase:

    def load_pickle(self, results_filename=None, base_dir=True):
        """
        load pickle file corresponding to caller test name
        """

        extension = ".pickle"

        # process caller
        if results_filename is None or base_dir:

            # retrieve results directory
            caller_filename = inspect.stack()[1].filename
            caller_directory = os.path.basename(os.path.dirname(caller_filename))

            # retrieve results filename
            if results_filename is None:
                caller_function = inspect.stack()[1].function
            else:
                caller_function = results_filename

            results_filename = f"tests/{caller_directory}/{caller_function}{extension}"

        return self.load_results(results_filename=results_filename,
                                 base_dir=False,
                                 extension=extension)

    def load_results(self, results_filename=None, base_dir=True, extension=".txt"):
        """
        load text file corresponding to caller test name
        """

        if results_filename is None or base_dir:

            # retrieve results directory
            caller_filename = inspect.stack()[1].filename
            caller_directory = os.path.basename(os.path.dirname(caller_filename))

            # retrieve results filename
            if results_filename is None:
                caller_function = inspect.stack()[1].function
            else:
                caller_function = results_filename

            results_filename = f"tests/{caller_directory}/{caller_function}{extension}"

        HANDLER = dict(
            txt=self._read_text,
            pickle=self._read_pickle)

        # read results
        dotless_extension = extension[1:]

        return HANDLER[dotless_extension](results_filename)

    def _read_text(self, filename):

        with open(filename) as file:
            results = file.read()

        return results.strip()

    def _read_pickle(self, filename):

        with open(filename, "rb") as file:
            content = pickle.load(file)

        return content

    def is_content_line(self, string, text):

        lines = text.split("\n")
        filtered = [line.strip() for line in lines if string == line.strip()]

        return len(filtered) > 0

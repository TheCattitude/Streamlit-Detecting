
from tests.test_base import TestBase


class TestPackageVersion(TestBase):

    def test_package_version(self):
        """
        verify that the package version of the challenge is correctly installed
        through `pip install -e .`
        and not one previous or later package version
        """

        package_summary = self.load_results()

        assert "api_pred" in package_summary, "the `taxifare` package version is not correct, please run `make reinstall_package` to reinstall the package"

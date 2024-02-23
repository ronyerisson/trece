from trece import PACKAGE_NAME


class TestSetupInstall:
    def test_addon_installed(self, installer):
        """Test if trece is installed."""
        assert installer.is_product_installed(PACKAGE_NAME) is True

    def test_browserlayer(self, browser_layers):
        """Test that ITreceLayer is registered."""
        from trece.interfaces import ITreceLayer

        assert ITreceLayer in browser_layers

    def test_latest_version(self, profile_last_version):
        """Test latest version of default profile."""
        assert profile_last_version(f"{PACKAGE_NAME}:default") == "20240223001"

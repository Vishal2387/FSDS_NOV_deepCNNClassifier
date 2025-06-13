import pytest
from deepClassifier.utils import read_yaml
from pathlib import Path
from box import ConfigBox
from ensure.main import EnsureError


class Test_read_yaml:
    yaml_files = [
        "tests/data/empty.yaml",
        "tests/data/demo.yaml"
    ]

    def test_read_yaml_empty(self):              ## is to test the empty data case in yaml
        with pytest.raises(ValueError):
            read_yaml(Path(self.yaml_files[0]))

    def test_read_yaml_return_type(self):
        respone = read_yaml(Path(self.yaml_files[-1]))
        assert isinstance(respone, ConfigBox)

    @pytest.mark.parametrize("path_to_yaml", yaml_files)   ## this will help us to give yaml files input as list
    def test_read_yaml_bad_type(self, path_to_yaml):      ## this test case is to test the path data type of yaml file 
        with pytest.raises(EnsureError):
            read_yaml(path_to_yaml)



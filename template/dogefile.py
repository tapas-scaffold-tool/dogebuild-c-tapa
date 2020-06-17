from pathlib import Path

from dogebuild_c.c_plugin import CPlugin, BinaryType


CPlugin(
    binary_type=BinaryType.EXECUTABLE,
    out_name="{{executable_name}}",
    src=Path("src").glob('**/*.c'),
    headers=Path("src").glob('**/*.h'),
)

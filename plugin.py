if "bpy" not in locals():
    print("load plugin")
    import bpy
    from .operators import WarCraft3OperatorImportMDX, WarCraft3OperatorAddSequenceToArmature, \
        WarCraft3OperatorRemoveSequenceToArmature, WarCraft3OperatorUpdateBoneSettings
    from .ui import WarCraft3PanelBone, WarCraft3PanelArmature
    from .preferences import WarCraft3Preferences
    from .props import WarCraft3ArmatureSequenceList, WarCraft3ArmatureProperties, WarCraft3BoneProperties
else:
    print("reload plugin")
    import importlib
    from . import operators
    from . import ui
    from . import preferences
    from . import props
    from .classes import classes_reload
    from . import constants
    from .importer import importer_reload
    from .mdx_parser import parser_reload, binary_reader
    from . import utils
    try:
        importlib.reload(operators)
        importlib.reload(ui)
        importlib.reload(preferences)
        importlib.reload(props)
        importlib.reload(binary_reader)
        importlib.reload(classes_reload)
        importlib.reload(constants)
        importlib.reload(importer_reload)
        importlib.reload(parser_reload)
        importlib.reload(utils)
    except ImportError:
        print("could not reload module")




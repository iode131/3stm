from guru.mappings import (
    ComboMapping,
    PluginParameterMapping,
    Control,
    MappingMode,
)
from functools import partial
from guru import observer


def cycle_flt1(): ...


def cycle_od(): ...


MAPPINGS = [
    MappingMode(
        [
            # SMEAR
            ComboMapping(
                mappings=[
                    PluginParameterMapping(
                        track_name="MAIN",
                        plugin_name="verb",
                        parameter_name="room_size",
                        controller_name="POT1",
                        preprocessor=lambda x: x,
                        parameter_label="Size",
                    ),
                    PluginParameterMapping(
                        "MAIN", "verb", "width", "POT1", lambda x: x, "Width"
                    ),
                    PluginParameterMapping(
                        "MAIN", "verb", "wet", "POT1", lambda x: x, "wet"
                    ),
                    PluginParameterMapping(
                        "MAIN", "verb", "dry", "POT1", lambda x: 1 - x, "dry"
                    ),
                ],
                controller_name="POT1",
                parameter_label="Smear",
            ),
            # SHAPE
            Control(controller_name="SW1", cb=cycle_flt1),
            PluginParameterMapping(
                "MAIN", "Filter1", "frequency", controller_name="ENC1"
            ),
            PluginParameterMapping("MAIN", "Filter1", "Q", controller_name="ENC2"),
            # SMASH
            Control("SW2", cycle_od),
            PluginParameterMapping(
                "MAIN", "cheap gain", "gain", controller_name="ENC3"
            ),
        ]
    )
]

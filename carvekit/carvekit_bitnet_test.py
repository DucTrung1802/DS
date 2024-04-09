from memory_profiler import profile
import PIL.Image
from enum import Enum
import torch
from carvekit.api.interface import Interface
from carvekit.ml.wrap.fba_matting import FBAMatting
from carvekit.ml.wrap.tracer_b7 import TracerUniversalB7
from carvekit.pipelines.postprocessing import MattingMethod
from carvekit.pipelines.preprocessing import PreprocessingStub
from carvekit.trimap.generator import TrimapGenerator


class SELCECTION(Enum):
    NORMAL_MODEL = "_NORMAL"
    HALF = "_HALF"
    _8_BIT = "_8_BIT"
    ONE_BIT = "_ONE_BIT"
    TWO_BIT = "_TWO_BIT"


# SETTING AREA ===============================================

INPUT_IMAGE_PATH = "car_1.jpg"


# CONSTANTS ==================================================

OUTPUT_IMAGE_EXTENSION = ".png"

FPA_MODEL_BASE_PATH = "./models/FBA"
SEG_NET_MODEL_BASE_PATH = "./models/SEG_NET"


# TEST_METHOD =================================================


@profile
def implement_test(selection: SELCECTION):
    value = selection.value
    print("\nTEST: MODEL" + value + " " + "=" * 50)
    fba_model = torch.load(FPA_MODEL_BASE_PATH + value)
    seg_net_model = torch.load(SEG_NET_MODEL_BASE_PATH + value)

    trimap = TrimapGenerator()

    preprocessing = PreprocessingStub()

    postprocessing = MattingMethod(
        matting_module=fba_model, trimap_generator=trimap, device="cpu"
    )

    interface = Interface(
        pre_pipe=preprocessing, post_pipe=postprocessing, seg_pipe=seg_net_model
    )

    image = PIL.Image.open(INPUT_IMAGE_PATH)
    cat_wo_bg = interface([image])[0]
    cat_wo_bg.save(INPUT_IMAGE_PATH.split(".")[0] + value + OUTPUT_IMAGE_EXTENSION)
    print()


def main():
    # implement_test(SELCECTION.<typename>)
    implement_test(SELCECTION.TWO_BIT)


if __name__ == "__main__":
    main()

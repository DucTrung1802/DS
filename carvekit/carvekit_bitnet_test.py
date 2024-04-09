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

from quant_linear import (
    create_quantized_copy_of_model,
    QuantizationMode,
)


class SELCECTION(Enum):
    NORMAL_MODEL = "_norm"
    HALF = "_half"
    _8_BIT = "_8_bit"
    ONE_BIT = "one_bit"
    TWO_BIT = "two_bit"


# SETTING AREA ===============================================

INPUT_IMAGE_PATH = "car_1.jpg"

OUTPUT_IMAGE_EXTENSION = ".png"
OUTPUT_NORM_IMAGE_NAME = (
    INPUT_IMAGE_PATH.split(".")[0]
    + SELCECTION.NORMAL_MODEL.value
    + OUTPUT_IMAGE_EXTENSION
)
OUTPUT_8_BIT_NAME = (
    INPUT_IMAGE_PATH.split(".")[0] + SELCECTION._8_BIT.value + OUTPUT_IMAGE_EXTENSION
)
OUTPUT_HALF_NAME = (
    INPUT_IMAGE_PATH.split(".")[0] + SELCECTION.HALF.value + OUTPUT_IMAGE_EXTENSION
)
OUTPUT_ONE_BIT_NAME = (
    INPUT_IMAGE_PATH.split(".")[0] + SELCECTION.ONE_BIT.value + OUTPUT_IMAGE_EXTENSION
)
OUTPUT_TWO_BIT_NAME = (
    INPUT_IMAGE_PATH.split(".")[0] + SELCECTION.TWO_BIT.value + OUTPUT_IMAGE_EXTENSION
)


@profile
def implement_test(selection: SELCECTION):
    match selection:
        case SELCECTION.NORMAL_MODEL:
            fba_model = torch.load()

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
    cat_wo_bg.save(output_file_path)


def main():
    # Check doc strings for more information

    FBA_PATH = "./models/FBA_NORMAL"

    SEG_NET_PATH = "./models/SEG_NET_NORMAL"

    NORMAL_FBA = FBAMatting(device="cpu", input_tensor_size=2048, batch_size=1)

    NORMAL_SEG_NET = TracerUniversalB7(device="cpu", batch_size=1)

    torch.save(NORMAL_FBA, FBA_PATH)

    torch.save(NORMAL_SEG_NET, SEG_NET_PATH)

    del NORMAL_FBA
    del NORMAL_SEG_NET

    NORMAL_FBA = torch.load(FBA_PATH)

    NORMAL_SEG_NET = torch.load(SEG_NET_PATH)

    print("NORMAL MODEL")
    # Normal model
    implement_test(
        fba_model=NORMAL_FBA,
        seg_net_model=NORMAL_SEG_NET,
        output_file_path=OUTPUT_NORM_IMAGE_NAME,
    )

    # # 8-bit quantized model
    # print("8-BIT MODEL")
    # quantized_implement_test(
    #     output_file_path=OUTPUT_8_BIT_NAME,
    # )

    # # one-bit quantized model
    # print("ONE-BIT MODEL")
    # one_bit_implement_test(
    #     output_file_path=OUTPUT_ONE_BIT_NAME,
    # )

    # # two-bit quantized model
    # print("TWO-BIT MODEL")
    # two_bit_implement_test(
    #     output_file_path=OUTPUT_TWO_BIT_NAME,
    # )


if __name__ == "__main__":
    main()

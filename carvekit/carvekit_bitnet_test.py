from memory_profiler import profile
import PIL.Image

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


# SETTING AREA ===============================================

INPUT_IMAGE_PATH = "car_1.jpg"

# ============================================================


OUTPUT_IMAGE_EXTENSION = ".png"
OUTPUT_NORM_IMAGE_NAME = (
    INPUT_IMAGE_PATH.split(".")[0] + "_norm" + OUTPUT_IMAGE_EXTENSION
)
OUTPUT_ONE_BIT_NAME = (
    INPUT_IMAGE_PATH.split(".")[0] + "_one_bit" + OUTPUT_IMAGE_EXTENSION
)
OUTPUT_TWO_BIT_NAME = (
    INPUT_IMAGE_PATH.split(".")[0] + "_two_bit" + OUTPUT_IMAGE_EXTENSION
)

NORMAL_FBA = FBAMatting(device="cpu", input_tensor_size=2048, batch_size=1)

NORMAL_SEG_NET = TracerUniversalB7(device="cpu", batch_size=1)

ONE_BIT_FBA = create_quantized_copy_of_model(
    NORMAL_FBA, quantization_mode=QuantizationMode.one_bit
)

ONE_BIT_SEG_NET = create_quantized_copy_of_model(
    NORMAL_SEG_NET, quantization_mode=QuantizationMode.one_bit
)


TWO_BIT_FBA = create_quantized_copy_of_model(
    NORMAL_FBA, quantization_mode=QuantizationMode.two_bit
)

TWO_BIT_SEG_NET = create_quantized_copy_of_model(
    NORMAL_SEG_NET, quantization_mode=QuantizationMode.two_bit
)


@profile
def normal_implement_test(input_image_path, output_file_path):

    trimap = TrimapGenerator()

    preprocessing = PreprocessingStub()

    postprocessing = MattingMethod(
        matting_module=NORMAL_FBA, trimap_generator=trimap, device="cpu"
    )

    interface = Interface(
        pre_pipe=preprocessing, post_pipe=postprocessing, seg_pipe=NORMAL_SEG_NET
    )

    image = PIL.Image.open(input_image_path)
    cat_wo_bg = interface([image])[0]
    cat_wo_bg.save(output_file_path)


@profile
def one_bit_implement_test(input_image_path, output_file_path):

    trimap = TrimapGenerator()

    preprocessing = PreprocessingStub()

    postprocessing = MattingMethod(
        matting_module=ONE_BIT_FBA, trimap_generator=trimap, device="cpu"
    )

    interface = Interface(
        pre_pipe=preprocessing, post_pipe=postprocessing, seg_pipe=ONE_BIT_SEG_NET
    )

    image = PIL.Image.open(input_image_path)
    cat_wo_bg = interface([image])[0]
    cat_wo_bg.save(output_file_path)


@profile
def two_bit_implement_test(input_image_path, output_file_path):

    trimap = TrimapGenerator()

    preprocessing = PreprocessingStub()

    postprocessing = MattingMethod(
        matting_module=TWO_BIT_FBA, trimap_generator=trimap, device="cpu"
    )

    interface = Interface(
        pre_pipe=preprocessing, post_pipe=postprocessing, seg_pipe=TWO_BIT_SEG_NET
    )

    image = PIL.Image.open(input_image_path)
    cat_wo_bg = interface([image])[0]
    cat_wo_bg.save(output_file_path)


def main():
    # Check doc strings for more information

    # print("NORMAL MODEL")
    # # Normal model
    # normal_implement_test(
    #     input_image_path=INPUT_IMAGE_PATH,
    #     output_file_path=OUTPUT_NORM_IMAGE_NAME,
    # )

    # # one-bit quantized model
    # print("ONE-BIT MODEL")
    # one_bit_implement_test(
    #     input_image_path=INPUT_IMAGE_PATH,
    #     output_file_path=OUTPUT_ONE_BIT_NAME,
    # )

    # two-bit quantized model
    print("TWO-BIT MODEL")
    two_bit_implement_test(
        input_image_path=INPUT_IMAGE_PATH,
        output_file_path=OUTPUT_TWO_BIT_NAME,
    )


if __name__ == "__main__":
    main()

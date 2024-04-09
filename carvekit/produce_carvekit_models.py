from memory_profiler import profile
import PIL.Image

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


# SETTING AREA ===============================================

# Normal model
FBA_NORMAL_PATH = "./models/FBA_NORMAL"
SEG_NORMAL_PATH = "./models/SEG_NET_NORMAL"

# Half datatype model (16-bit)
FBA_HALF_PATH = "./models/FBA_TORCH_HALF"
SEG_NET_HALF_PATH = "./models/SEG_NET_TORCH_HALF"

# Torch 8-bit model
FBA_8_BIT_PATH = "./models/FBA_8_BIT"
SEG_NET_8_BIT_PATH = "./models/SEG_NET_8_BIT"

# One bit model
FBA_ONE_BIT_PATH = "./models/FBA_ONE_BIT"
SEG_NET_ONE_BIT_PATH = "./models/SEG_NET_ONE_BIT"

# Two bit model
FBA_TWO_BIT_PATH = "./models/FBA_TWO_BIT"
SEG_NET_TWO_BIT_PATH = "./models/SEG_NET_TWO_BIT"


# MODELS =====================================================

# Normal model
FBA_NORMAL = FBAMatting(device="cpu", input_tensor_size=2048, batch_size=1)
SEG_NET_NORMAL = TracerUniversalB7(device="cpu", batch_size=1)

# Half datatype model (16-bit)
FBA_HALF = FBAMatting(device="cpu", input_tensor_size=2048, batch_size=1).half()
SEG_NET_HALF = TracerUniversalB7(device="cpu", batch_size=1).half()

# Torch 8-bit model
FBA_8_BIT = torch.quantization.quantize_dynamic(model=FBA_NORMAL, dtype=torch.qint8)
SEG_NET_8_BIT = torch.quantization.quantize_dynamic(
    model=SEG_NET_NORMAL, dtype=torch.qint8
)

# One bit model
FBA_ONE_BIT = create_quantized_copy_of_model(
    FBA_NORMAL, quantization_mode=QuantizationMode.one_bit
)
SEG_NET_ONE_BIT = create_quantized_copy_of_model(
    SEG_NET_NORMAL, quantization_mode=QuantizationMode.one_bit
)

# Two bit model
FBA_TWO_BIT = create_quantized_copy_of_model(
    FBA_NORMAL, quantization_mode=QuantizationMode.two_bit
)
SEG_NET_TWO_BIT = create_quantized_copy_of_model(
    SEG_NET_NORMAL, quantization_mode=QuantizationMode.two_bit
)


def main():
    # Check doc strings for more information

    # Normal model
    torch.save(FBA_NORMAL, FBA_NORMAL_PATH)
    torch.save(SEG_NET_NORMAL, SEG_NORMAL_PATH)

    # Half datatype model (16-bit)
    torch.save(FBA_HALF, FBA_HALF_PATH)
    torch.save(SEG_NET_HALF, SEG_NET_HALF_PATH)

    # Torch 8-bit model
    torch.save(FBA_8_BIT, FBA_8_BIT_PATH)
    torch.save(SEG_NET_8_BIT, SEG_NET_8_BIT_PATH)

    # One bit model
    torch.save(FBA_ONE_BIT, FBA_ONE_BIT_PATH)
    torch.save(SEG_NET_ONE_BIT, SEG_NET_ONE_BIT_PATH)

    # Two bit model
    torch.save(FBA_TWO_BIT, FBA_TWO_BIT_PATH)
    torch.save(SEG_NET_TWO_BIT, SEG_NET_TWO_BIT_PATH)


if __name__ == "__main__":
    main()

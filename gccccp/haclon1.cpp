
#include "HalconCpp.h"

#include <iostream>

int main(int argc, char **argv)
{
    HalconCpp::HObject hobj;
    HalconCpp::HTuple width, height;
    HalconCpp::ReadImage(&hobj, "printer_chip/printer_chip_01");
    HalconCpp::GetImageSize(hobj, &width, &height);

    std::cout << "Image - width: " << width.I() << ", height: " << height.I() << std::endl;
    return 0;
}

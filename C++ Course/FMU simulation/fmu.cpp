#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <dlfcn.h>  // Use LoadLibrary on Windows
#include "fmi3Functions.h"

// Define function pointers according to the FMI standard
typedef fmi3Component (*fmi3InstantiateFunc)(const char*, fmi3Type, const char*, const char*, const fmi3CallbackFunctions*, fmi3Boolean, fmi3Boolean);
typedef fmi3Status (*fmi3DoStepFunc)(fmi3Component, fmi3Real, fmi3Real, fmi3Boolean);
typedef fmi3Status (*fmi3SetRealFunc)(fmi3Component, const fmi3ValueReference*, size_t, const fmi3Real*);
typedef fmi3Status (*fmi3GetRealFunc)(fmi3Component, const fmi3ValueReference*, size_t, fmi3Real*);
typedef void (*fmi3FreeInstanceFunc)(fmi3Component);

void simulateFMU(const std::string &fmuPath) {
    // Load the FMU shared library (Linux/macOS). On Windows, use LoadLibrary.
    void* handle = dlopen((fmuPath + "/binaries/linux64/model.so").c_str(), RTLD_LAZY);
    if (!handle) {
        std::cerr << "Error loading FMU shared library: " << dlerror() << std::endl;
        return;
    }

    // Load FMI functions
    auto fmi3Instantiate = (fmi3InstantiateFunc)dlsym(handle, "fmi3Instantiate");
    auto fmi3DoStep = (fmi3DoStepFunc)dlsym(handle, "fmi3DoStep");
    auto fmi3SetReal = (fmi3SetRealFunc)dlsym(handle, "fmi3SetReal");
    auto fmi3GetReal = (fmi3GetRealFunc)dlsym(handle, "fmi3GetReal");
    auto fmi3FreeInstance = (fmi3FreeInstanceFunc)dlsym(handle, "fmi3FreeInstance");

    if (!fmi3Instantiate || !fmi3DoStep || !fmi3SetReal || !fmi3GetReal || !fmi3FreeInstance) {
        std::cerr << "Error loading FMI functions." << std::endl;
        dlclose(handle);
        return;
    }

    // Instantiate FMU
    fmi3CallbackFunctions callbacks = {nullptr, nullptr, nullptr, nullptr, nullptr};
    fmi3Component fmu = fmi3Instantiate("MyFMU", fmi3CoSimulation, nullptr, nullptr, &callbacks, fmi3False, fmi3False);
    if (!fmu) {
        std::cerr << "Failed to instantiate FMU." << std::endl;
        dlclose(handle);
        return;
    }

    // Simulation parameters
    fmi3Real startTime = 0.0;
    fmi3Real stopTime = 1.0;
    fmi3Real stepSize = 0.1;
    fmi3Real currentTime = startTime;

    // Set an input (Example: Value Reference 0 = Input)
    fmi3ValueReference inputRef = 0;
    fmi3Real inputValue = 1.0;
    fmi3SetReal(fmu, &inputRef, 1, &inputValue);

    // Simulation loop
    while (currentTime < stopTime) {
        fmi3DoStep(fmu, currentTime, stepSize, fmi3True);

        // Read output (Example: Value Reference 1 = Output)
        fmi3ValueReference outputRef = 1;
        fmi3Real outputValue;
        fmi3GetReal(fmu, &outputRef, 1, &outputValue);

        std::cout << "Time: " << currentTime << ", Output: " << outputValue << std::endl;
        currentTime += stepSize;
    }

    // Cleanup
    fmi3FreeInstance(fmu);
    dlclose(handle);
}

int main() {
    std::string fmuPath = "path/to/extracted/fmu"; // Update this path
    simulateFMU(fmuPath);
    return 0;
}

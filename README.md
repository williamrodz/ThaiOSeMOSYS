This repository is an effort to keep track of scenario runs for Thailand net zero modelling. 
The following is a description of this repository's folders and its contents:

#### `ThaiStarterKitFiles/`
- Includes the group of files provided by the OSeMOSYS group outlining the Thailand Net Zero, Least Cost, and Fossil Future scenarios
- These files should NOT be modified and should be a base of comparison against our own scenarios

#### `OSeMOSYSModelLibrary/`
- Includes versions of the OSeMOSYS model that is used to optimize an energy system

#### `CustomThailandScenarios/`
- This is where we will store scenario files that we have manipulated.
- Each file scenario here should be named with a descriptive short name and be accompanied with a markdown file that will provide a more detailed description of the scenario
  - e.g. `DoublePadThaiScenario.xlsm`: scenario file, `DoublePadThaiScenario.md`: description file.  


# Get Started

Begin by cloning the repository to your computer
```
cd <folder of your choosing>
git clone <insert .git URL from this repo>
```

When you create a new scenario, make sure to place it in `CustomThailandScenarios/`, with accompanying files.

You may optionally copy the unfiltered parameters sheet into a CSV so that you can compare it against
the base parameters file from the Net Zero Scenario. This is the `Thailand_NZv2_PARAM.csv` file in `ThaiStarterKitFiles`.

The file structure for each added scenario should look like this:
```
CustomThailandScenarios/
  ...
  MyScenarioSAND.xlsm
  MyScenarioDescription.md
  (Optional) MyScenarioPARAM.csv
  ...
```

  





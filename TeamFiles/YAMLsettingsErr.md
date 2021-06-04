[OLD] as of new we have 3.24 rated code
2s
Run pylint `ls -R|grep .py$|xargs`
************* Module AppJarTest
AppJarTest.py:1:0: C0103: Module name "AppJarTest" doesn't conform to snake_case naming style (invalid-name)
AppJarTest.py:1:0: C0114: Missing module docstring (missing-module-docstring)
AppJarTest.py:2:0: E0401: Unable to import 'appJar' (import-error)
AppJarTest.py:9:0: C0116: Missing function or method docstring (missing-function-docstring)
************* Module main
main.py:2:19: C0303: Trailing whitespace (trailing-whitespace)
main.py:37:1: W0511: TODO:fix app icon (fixme)
main.py:39:1: W0511: TODO: document all new dependencies (fixme)
main.py:53:1: W0511: TODO:fix app icon (fixme)
main.py:1:0: C0114: Missing module docstring (missing-module-docstring)
main.py:2:0: E0401: Unable to import 'pandas' (import-error)
main.py:3:0: E0401: Unable to import 'numpy' (import-error)
main.py:4:0: E0401: Unable to import 'appJar' (import-error)
main.py:9:0: E0401: Unable to import 'matplotlib' (import-error)
main.py:10:0: E0401: Unable to import 'yaml' (import-error)
main.py:24:0: R1732: Consider using 'with' for resource-allocating operations (consider-using-with)
main.py:45:0: R1732: Consider using 'with' for resource-allocating operations (consider-using-with)
main.py:2:0: W0611: Unused pandas imported as pd (unused-import)
main.py:3:0: W0611: Unused numpy imported as np (unused-import)
main.py:5:0: W0611: Unused import statistics (unused-import)
main.py:6:0: W0611: Unused import random (unused-import)
main.py:7:0: W0611: Unused import os (unused-import)
main.py:8:0: W0611: Unused import sys (unused-import)
main.py:9:0: W0611: Unused matplotlib imported as plt (unused-import)
main.py:5:0: C0411: standard import "import statistics" should be placed before "import pandas as pd" (wrong-import-order)
main.py:6:0: C0411: standard import "import random" should be placed before "import pandas as pd" (wrong-import-order)
main.py:7:0: C0411: standard import "import os" should be placed before "import pandas as pd" (wrong-import-order)
main.py:8:0: C0411: standard import "import sys" should be placed before "import pandas as pd" (wrong-import-order)

------------------------------------
Your code has been rated at -1.59/10

Error: Process completed with exit code 30

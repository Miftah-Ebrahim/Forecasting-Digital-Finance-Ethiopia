import json
import os

nb_path = "notebooks/01_exploration_eda.ipynb"
project_root = (
    r"C:\Users\hp\Downloads\KAIM\KAIM WEEK 10\Forecasting-Digital-Finance-Ethiopia"
)
src_path = os.path.join(project_root, "src").replace("\\", "/")

with open(nb_path, "r", encoding="utf-8") as f:
    nb = json.load(f)

# Remove the broken cell if it exists (check first source line import sys)
if (
    nb["cells"][0]["source"][0] == "import sys\n"
    and "sys.path.append" in nb["cells"][0]["source"][2]
):
    nb["cells"].pop(0)

# Add a specific setup cell at the top
setup_cell = {
    "cell_type": "code",
    "execution_count": None,
    "metadata": {},
    "outputs": [],
    "source": [
        "import sys\n",
        "import os\n",
        f"sys.path.append(r'{src_path}')\n",
        f"print(f'Added {src_path} to sys.path')\n",
    ],
}

nb["cells"].insert(0, setup_cell)

with open(nb_path, "w", encoding="utf-8") as f:
    json.dump(nb, f, indent=1)

print("Added absolute path setup to notebook.")

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
source "$SCRIPT_DIR/.venv/bin/activate"

black "$SCRIPT_DIR/simtrain_eco_mini_app_streamlit_sdk/services/resources/"*.py
black "$SCRIPT_DIR/simtrain_eco_mini_app_streamlit_sdk/sdk.py"

deactivate
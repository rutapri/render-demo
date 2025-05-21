{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "e30f186b-c3eb-49e2-9165-bbb9a05138f0",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "\n",
       "        <iframe\n",
       "            width=\"100%\"\n",
       "            height=\"650\"\n",
       "            src=\"http://127.0.0.1:8050/\"\n",
       "            frameborder=\"0\"\n",
       "            allowfullscreen\n",
       "            \n",
       "        ></iframe>\n",
       "        "
      ],
      "text/plain": [
       "<IPython.lib.display.IFrame at 0x17f5a803590>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "import dash\n",
    "from dash import dcc, html\n",
    "import plotly.express as px\n",
    "import pandas as pd\n",
    "\n",
    "# Load CSV\n",
    "def load_data():\n",
    "    df = pd.read_csv(\"rawdata_test.csv\", parse_dates=[\"Date\"], index_col=\"Date\")\n",
    "    df = df.reset_index()\n",
    "    return df\n",
    "\n",
    "# Load and prep data\n",
    "df = load_data()\n",
    "\n",
    "# Dash app\n",
    "app = dash.Dash(__name__)\n",
    "\n",
    "server = app.server\n",
    "\n",
    "app.title = \"EURUSD-SPX Correlation\"\n",
    "\n",
    "# Line chart\n",
    "fig = px.line(df, x=\"Date\", y=\"EURUSD\", title=\"EURUSD-SPX Correlation Over Time\")\n",
    "\n",
    "# Layout\n",
    "app.layout = html.Div([\n",
    "    html.H1(\"Correlation Dashboard\", style={'textAlign': 'center'}),\n",
    "    dcc.Graph(figure=fig)\n",
    "])\n",
    "\n",
    "# Optional: local debug\n",
    "if __name__ == \"__main__\":\n",
    "    app.run(host=\"0.0.0.0\", port=8050, debug=True)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}

{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "82a35d0c-2347-4285-8626-832d518c65da",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Collecting dash\n",
      "  Using cached dash-3.0.4-py3-none-any.whl.metadata (10 kB)\n",
      "Requirement already satisfied: plotly in c:\\users\\rutaprieskienyte\\anaconda3\\lib\\site-packages (5.22.0)\n",
      "Requirement already satisfied: pandas in c:\\users\\rutaprieskienyte\\anaconda3\\lib\\site-packages (2.2.2)\n",
      "Requirement already satisfied: Flask<3.1,>=1.0.4 in c:\\users\\rutaprieskienyte\\anaconda3\\lib\\site-packages (from dash) (3.0.3)\n",
      "Requirement already satisfied: Werkzeug<3.1 in c:\\users\\rutaprieskienyte\\anaconda3\\lib\\site-packages (from dash) (3.0.3)\n",
      "Requirement already satisfied: importlib-metadata in c:\\users\\rutaprieskienyte\\anaconda3\\lib\\site-packages (from dash) (7.0.1)\n",
      "Requirement already satisfied: typing-extensions>=4.1.1 in c:\\users\\rutaprieskienyte\\anaconda3\\lib\\site-packages (from dash) (4.11.0)\n",
      "Requirement already satisfied: requests in c:\\users\\rutaprieskienyte\\anaconda3\\lib\\site-packages (from dash) (2.32.2)\n",
      "Collecting retrying (from dash)\n",
      "  Using cached retrying-1.3.4-py3-none-any.whl.metadata (6.9 kB)\n",
      "Requirement already satisfied: nest-asyncio in c:\\users\\rutaprieskienyte\\anaconda3\\lib\\site-packages (from dash) (1.6.0)\n",
      "Requirement already satisfied: setuptools in c:\\users\\rutaprieskienyte\\anaconda3\\lib\\site-packages (from dash) (69.5.1)\n",
      "Requirement already satisfied: tenacity>=6.2.0 in c:\\users\\rutaprieskienyte\\anaconda3\\lib\\site-packages (from plotly) (8.2.2)\n",
      "Requirement already satisfied: packaging in c:\\users\\rutaprieskienyte\\anaconda3\\lib\\site-packages (from plotly) (23.2)\n",
      "Requirement already satisfied: numpy>=1.26.0 in c:\\users\\rutaprieskienyte\\anaconda3\\lib\\site-packages (from pandas) (1.26.4)\n",
      "Requirement already satisfied: python-dateutil>=2.8.2 in c:\\users\\rutaprieskienyte\\anaconda3\\lib\\site-packages (from pandas) (2.9.0.post0)\n",
      "Requirement already satisfied: pytz>=2020.1 in c:\\users\\rutaprieskienyte\\anaconda3\\lib\\site-packages (from pandas) (2024.1)\n",
      "Requirement already satisfied: tzdata>=2022.7 in c:\\users\\rutaprieskienyte\\anaconda3\\lib\\site-packages (from pandas) (2023.3)\n",
      "Requirement already satisfied: Jinja2>=3.1.2 in c:\\users\\rutaprieskienyte\\anaconda3\\lib\\site-packages (from Flask<3.1,>=1.0.4->dash) (3.1.4)\n",
      "Requirement already satisfied: itsdangerous>=2.1.2 in c:\\users\\rutaprieskienyte\\anaconda3\\lib\\site-packages (from Flask<3.1,>=1.0.4->dash) (2.2.0)\n",
      "Requirement already satisfied: click>=8.1.3 in c:\\users\\rutaprieskienyte\\anaconda3\\lib\\site-packages (from Flask<3.1,>=1.0.4->dash) (8.1.7)\n",
      "Requirement already satisfied: blinker>=1.6.2 in c:\\users\\rutaprieskienyte\\anaconda3\\lib\\site-packages (from Flask<3.1,>=1.0.4->dash) (1.6.2)\n",
      "Requirement already satisfied: six>=1.5 in c:\\users\\rutaprieskienyte\\anaconda3\\lib\\site-packages (from python-dateutil>=2.8.2->pandas) (1.16.0)\n",
      "Requirement already satisfied: MarkupSafe>=2.1.1 in c:\\users\\rutaprieskienyte\\anaconda3\\lib\\site-packages (from Werkzeug<3.1->dash) (2.1.3)\n",
      "Requirement already satisfied: zipp>=0.5 in c:\\users\\rutaprieskienyte\\anaconda3\\lib\\site-packages (from importlib-metadata->dash) (3.17.0)\n",
      "Requirement already satisfied: charset-normalizer<4,>=2 in c:\\users\\rutaprieskienyte\\anaconda3\\lib\\site-packages (from requests->dash) (2.0.4)\n",
      "Requirement already satisfied: idna<4,>=2.5 in c:\\users\\rutaprieskienyte\\anaconda3\\lib\\site-packages (from requests->dash) (3.7)\n",
      "Requirement already satisfied: urllib3<3,>=1.21.1 in c:\\users\\rutaprieskienyte\\anaconda3\\lib\\site-packages (from requests->dash) (2.2.2)\n",
      "Requirement already satisfied: certifi>=2017.4.17 in c:\\users\\rutaprieskienyte\\anaconda3\\lib\\site-packages (from requests->dash) (2024.8.30)\n",
      "Requirement already satisfied: colorama in c:\\users\\rutaprieskienyte\\anaconda3\\lib\\site-packages (from click>=8.1.3->Flask<3.1,>=1.0.4->dash) (0.4.6)\n",
      "Using cached dash-3.0.4-py3-none-any.whl (7.9 MB)\n",
      "Using cached retrying-1.3.4-py3-none-any.whl (11 kB)\n",
      "Installing collected packages: retrying, dash\n",
      "Successfully installed dash-3.0.4 retrying-1.3.4\n",
      "Note: you may need to restart the kernel to use updated packages.\n"
     ]
    }
   ],
   "source": [
    "pip install dash plotly pandas"
   ]
  },
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
    "df = pd.read_csv(\"C:\\\\Users\\\\RutaPrieskienyte\\\\FX analysis\\\\rawdata_test.csv\", parse_dates=[\"Date\"], index_col=\"Date\")\n",
    "df = df.reset_index()  # Convert index to column so Plotly can use it\n",
    "\n",
    "# Initialize app\n",
    "app = dash.Dash(__name__)\n",
    "app.title = \"EURUSD-SPX Correlation\"\n",
    "\n",
    "# Create figure\n",
    "fig = px.line(df, x=\"Date\", y=\"EURUSD\", title=\"EURUSD-SPX Correlation Over Time\")\n",
    "\n",
    "# Layout\n",
    "app.layout = html.Div([\n",
    "    html.H1(\"Correlation Dashboard\", style={'textAlign': 'center'}),\n",
    "    dcc.Graph(figure=fig)\n",
    "])\n",
    "\n",
    "# Run the app on host='0.0.0.0' to allow LAN access\n",
    "if __name__ == '__main__':\n",
    "    app.run(host=\"127.0.0.1\", port=8050, debug=True)"
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

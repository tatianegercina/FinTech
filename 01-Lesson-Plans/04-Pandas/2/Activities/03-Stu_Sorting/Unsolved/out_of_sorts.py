{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "from pathlib import Path"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Symbol</th>\n",
       "      <th>Trade DATE</th>\n",
       "      <th>NOCP</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>TSLA</td>\n",
       "      <td>5/14/2019</td>\n",
       "      <td>232.31</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>TSLA</td>\n",
       "      <td>5/13/2019</td>\n",
       "      <td>227.01</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>TSLA</td>\n",
       "      <td>5/10/2019</td>\n",
       "      <td>239.52</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>TSLA</td>\n",
       "      <td>5/9/2019</td>\n",
       "      <td>241.98</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>TSLA</td>\n",
       "      <td>5/8/2019</td>\n",
       "      <td>244.84</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "  Symbol Trade DATE    NOCP\n",
       "0   TSLA  5/14/2019  232.31\n",
       "1   TSLA  5/13/2019  227.01\n",
       "2   TSLA  5/10/2019  239.52\n",
       "3   TSLA   5/9/2019  241.98\n",
       "4   TSLA   5/8/2019  244.84"
      ]
     },
     "execution_count": 2,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Read in csv\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Index data by `Trade DATE`"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Symbol</th>\n",
       "      <th>NOCP</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Trade DATE</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>5/14/2019</th>\n",
       "      <td>TSLA</td>\n",
       "      <td>232.31</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5/13/2019</th>\n",
       "      <td>TSLA</td>\n",
       "      <td>227.01</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5/10/2019</th>\n",
       "      <td>TSLA</td>\n",
       "      <td>239.52</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5/9/2019</th>\n",
       "      <td>TSLA</td>\n",
       "      <td>241.98</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5/8/2019</th>\n",
       "      <td>TSLA</td>\n",
       "      <td>244.84</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "           Symbol    NOCP\n",
       "Trade DATE               \n",
       "5/14/2019    TSLA  232.31\n",
       "5/13/2019    TSLA  227.01\n",
       "5/10/2019    TSLA  239.52\n",
       "5/9/2019     TSLA  241.98\n",
       "5/8/2019     TSLA  244.84"
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": []
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Assess and clean data"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>NOCP</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Trade DATE</th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>5/14/2019</th>\n",
       "      <td>232.31</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5/13/2019</th>\n",
       "      <td>227.01</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5/10/2019</th>\n",
       "      <td>239.52</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5/9/2019</th>\n",
       "      <td>241.98</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5/8/2019</th>\n",
       "      <td>244.84</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "              NOCP\n",
       "Trade DATE        \n",
       "5/14/2019   232.31\n",
       "5/13/2019   227.01\n",
       "5/10/2019   239.52\n",
       "5/9/2019    241.98\n",
       "5/8/2019    244.84"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Check for nulls\n",
    "\n",
    "# Drop missing values\n",
    "\n",
    "# Validate no more missing values\n",
    "\n",
    "# Drop unnecessary columns\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Calculate daily returns"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>NOCP</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Trade DATE</th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>5/14/2019</th>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5/13/2019</th>\n",
       "      <td>-0.022814</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5/10/2019</th>\n",
       "      <td>0.055108</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5/9/2019</th>\n",
       "      <td>0.010271</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5/8/2019</th>\n",
       "      <td>0.011819</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                NOCP\n",
       "Trade DATE          \n",
       "5/14/2019        NaN\n",
       "5/13/2019  -0.022814\n",
       "5/10/2019   0.055108\n",
       "5/9/2019    0.010271\n",
       "5/8/2019    0.011819"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": []
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Sort the DataFrame by `NOCP` in descending order using `sort_values`."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>NOCP</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Trade DATE</th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>1/17/2019</th>\n",
       "      <td>0.149044</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4/3/2019</th>\n",
       "      <td>0.089738</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2/28/2019</th>\n",
       "      <td>0.085111</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>12/21/2018</th>\n",
       "      <td>0.082535</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>12/31/2018</th>\n",
       "      <td>0.073133</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                NOCP\n",
       "Trade DATE          \n",
       "1/17/2019   0.149044\n",
       "4/3/2019    0.089738\n",
       "2/28/2019   0.085111\n",
       "12/21/2018  0.082535\n",
       "12/31/2018  0.073133"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": []
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Slice out 5 records"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>NOCP</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Trade DATE</th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>1/17/2019</th>\n",
       "      <td>0.149044</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4/3/2019</th>\n",
       "      <td>0.089738</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2/28/2019</th>\n",
       "      <td>0.085111</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>12/21/2018</th>\n",
       "      <td>0.082535</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>12/31/2018</th>\n",
       "      <td>0.073133</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                NOCP\n",
       "Trade DATE          \n",
       "1/17/2019   0.149044\n",
       "4/3/2019    0.089738\n",
       "2/28/2019   0.085111\n",
       "12/21/2018  0.082535\n",
       "12/31/2018  0.073133"
      ]
     },
     "execution_count": 16,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": []
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Plot top 5 performing days for TSLA investment returns"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<matplotlib.axes._subplots.AxesSubplot at 0x21b6f2d89b0>"
      ]
     },
     "execution_count": 26,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
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
   "version": "3.7.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}

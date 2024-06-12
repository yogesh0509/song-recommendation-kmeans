{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Collecting nbformat\n",
      "  Using cached nbformat-5.10.4-py3-none-any.whl.metadata (3.6 kB)\n",
      "Requirement already satisfied: ipython in ./.venv/lib/python3.11/site-packages (8.25.0)\n",
      "Collecting fastjsonschema>=2.15 (from nbformat)\n",
      "  Using cached fastjsonschema-2.19.1-py3-none-any.whl.metadata (2.1 kB)\n",
      "Collecting jsonschema>=2.6 (from nbformat)\n",
      "  Using cached jsonschema-4.22.0-py3-none-any.whl.metadata (8.2 kB)\n",
      "Requirement already satisfied: jupyter-core!=5.0.*,>=4.12 in ./.venv/lib/python3.11/site-packages (from nbformat) (5.7.2)\n",
      "Requirement already satisfied: traitlets>=5.1 in ./.venv/lib/python3.11/site-packages (from nbformat) (5.14.3)\n",
      "Requirement already satisfied: decorator in ./.venv/lib/python3.11/site-packages (from ipython) (5.1.1)\n",
      "Requirement already satisfied: jedi>=0.16 in ./.venv/lib/python3.11/site-packages (from ipython) (0.19.1)\n",
      "Requirement already satisfied: matplotlib-inline in ./.venv/lib/python3.11/site-packages (from ipython) (0.1.7)\n",
      "Requirement already satisfied: prompt-toolkit<3.1.0,>=3.0.41 in ./.venv/lib/python3.11/site-packages (from ipython) (3.0.46)\n",
      "Requirement already satisfied: pygments>=2.4.0 in ./.venv/lib/python3.11/site-packages (from ipython) (2.18.0)\n",
      "Requirement already satisfied: stack-data in ./.venv/lib/python3.11/site-packages (from ipython) (0.6.3)\n",
      "Requirement already satisfied: typing-extensions>=4.6 in ./.venv/lib/python3.11/site-packages (from ipython) (4.12.2)\n",
      "Requirement already satisfied: pexpect>4.3 in ./.venv/lib/python3.11/site-packages (from ipython) (4.9.0)\n",
      "Requirement already satisfied: parso<0.9.0,>=0.8.3 in ./.venv/lib/python3.11/site-packages (from jedi>=0.16->ipython) (0.8.4)\n",
      "Collecting attrs>=22.2.0 (from jsonschema>=2.6->nbformat)\n",
      "  Using cached attrs-23.2.0-py3-none-any.whl.metadata (9.5 kB)\n",
      "Collecting jsonschema-specifications>=2023.03.6 (from jsonschema>=2.6->nbformat)\n",
      "  Using cached jsonschema_specifications-2023.12.1-py3-none-any.whl.metadata (3.0 kB)\n",
      "Collecting referencing>=0.28.4 (from jsonschema>=2.6->nbformat)\n",
      "  Using cached referencing-0.35.1-py3-none-any.whl.metadata (2.8 kB)\n",
      "Collecting rpds-py>=0.7.1 (from jsonschema>=2.6->nbformat)\n",
      "  Using cached rpds_py-0.18.1-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (4.1 kB)\n",
      "Requirement already satisfied: platformdirs>=2.5 in ./.venv/lib/python3.11/site-packages (from jupyter-core!=5.0.*,>=4.12->nbformat) (4.2.2)\n",
      "Requirement already satisfied: ptyprocess>=0.5 in ./.venv/lib/python3.11/site-packages (from pexpect>4.3->ipython) (0.7.0)\n",
      "Requirement already satisfied: wcwidth in ./.venv/lib/python3.11/site-packages (from prompt-toolkit<3.1.0,>=3.0.41->ipython) (0.2.13)\n",
      "Requirement already satisfied: executing>=1.2.0 in ./.venv/lib/python3.11/site-packages (from stack-data->ipython) (2.0.1)\n",
      "Requirement already satisfied: asttokens>=2.1.0 in ./.venv/lib/python3.11/site-packages (from stack-data->ipython) (2.4.1)\n",
      "Requirement already satisfied: pure-eval in ./.venv/lib/python3.11/site-packages (from stack-data->ipython) (0.2.2)\n",
      "Requirement already satisfied: six>=1.12.0 in ./.venv/lib/python3.11/site-packages (from asttokens>=2.1.0->stack-data->ipython) (1.16.0)\n",
      "Using cached nbformat-5.10.4-py3-none-any.whl (78 kB)\n",
      "Using cached fastjsonschema-2.19.1-py3-none-any.whl (23 kB)\n",
      "Using cached jsonschema-4.22.0-py3-none-any.whl (88 kB)\n",
      "Using cached attrs-23.2.0-py3-none-any.whl (60 kB)\n",
      "Using cached jsonschema_specifications-2023.12.1-py3-none-any.whl (18 kB)\n",
      "Using cached referencing-0.35.1-py3-none-any.whl (26 kB)\n",
      "Using cached rpds_py-0.18.1-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (1.1 MB)\n",
      "Installing collected packages: fastjsonschema, rpds-py, attrs, referencing, jsonschema-specifications, jsonschema, nbformat\n",
      "Successfully installed attrs-23.2.0 fastjsonschema-2.19.1 jsonschema-4.22.0 jsonschema-specifications-2023.12.1 nbformat-5.10.4 referencing-0.35.1 rpds-py-0.18.1\n"
     ]
    }
   ],
   "source": [
    "! pip install nbformat ipython"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " * Serving Flask app '__main__'\n",
      " * Debug mode: on\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "\u001b[31m\u001b[1mWARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.\u001b[0m\n",
      " * Running on http://127.0.0.1:5001\n",
      "\u001b[33mPress CTRL+C to quit\u001b[0m\n",
      " * Restarting with stat\n",
      "Traceback (most recent call last):\n",
      "  File \"<frozen runpy>\", line 198, in _run_module_as_main\n",
      "  File \"<frozen runpy>\", line 88, in _run_code\n",
      "  File \"/home/yogesh/Desktop/Personal/VI SEM PROJECT/.venv/lib/python3.11/site-packages/ipykernel_launcher.py\", line 18, in <module>\n",
      "    app.launch_new_instance()\n",
      "  File \"/home/yogesh/Desktop/Personal/VI SEM PROJECT/.venv/lib/python3.11/site-packages/traitlets/config/application.py\", line 1074, in launch_instance\n",
      "    app.initialize(argv)\n",
      "  File \"/home/yogesh/Desktop/Personal/VI SEM PROJECT/.venv/lib/python3.11/site-packages/traitlets/config/application.py\", line 118, in inner\n",
      "    return method(app, *args, **kwargs)\n",
      "           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n",
      "  File \"/home/yogesh/Desktop/Personal/VI SEM PROJECT/.venv/lib/python3.11/site-packages/ipykernel/kernelapp.py\", line 692, in initialize\n",
      "    self.init_sockets()\n",
      "  File \"/home/yogesh/Desktop/Personal/VI SEM PROJECT/.venv/lib/python3.11/site-packages/ipykernel/kernelapp.py\", line 331, in init_sockets\n",
      "    self.shell_port = self._bind_socket(self.shell_socket, self.shell_port)\n",
      "                      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n",
      "  File \"/home/yogesh/Desktop/Personal/VI SEM PROJECT/.venv/lib/python3.11/site-packages/ipykernel/kernelapp.py\", line 253, in _bind_socket\n",
      "    return self._try_bind_socket(s, port)\n",
      "           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n",
      "  File \"/home/yogesh/Desktop/Personal/VI SEM PROJECT/.venv/lib/python3.11/site-packages/ipykernel/kernelapp.py\", line 229, in _try_bind_socket\n",
      "    s.bind(\"tcp://%s:%i\" % (self.ip, port))\n",
      "  File \"/home/yogesh/Desktop/Personal/VI SEM PROJECT/.venv/lib/python3.11/site-packages/zmq/sugar/socket.py\", line 311, in bind\n",
      "    super().bind(addr)\n",
      "  File \"_zmq.py\", line 898, in zmq.backend.cython._zmq.Socket.bind\n",
      "  File \"_zmq.py\", line 160, in zmq.backend.cython._zmq._check_rc\n",
      "zmq.error.ZMQError: Address already in use (addr='tcp://127.0.0.1:9002')\n"
     ]
    },
    {
     "ename": "SystemExit",
     "evalue": "1",
     "output_type": "error",
     "traceback": [
      "An exception has occurred, use %tb to see the full traceback.\n",
      "\u001b[0;31mSystemExit\u001b[0m\u001b[0;31m:\u001b[0m 1\n"
     ]
    }
   ],
   "source": [
    "from flask import Flask, jsonify\n",
    "from flask_cors import CORS\n",
    "import json\n",
    "\n",
    "app = Flask(__name__)\n",
    "CORS(app)\n",
    "\n",
    "@app.route('/recommend', methods=['GET'])\n",
    "def recommend():\n",
    "    with open('recommended_songs.json', 'r') as file:\n",
    "        recommended_songs = json.load(file)\n",
    "    return jsonify(recommended_songs)\n",
    "\n",
    "if __name__ == '__main__':\n",
    "    app.run(debug=True, port=5001)  # Change the port to an available one\n"
   ]
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
   "display_name": ".venv",
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
   "version": "3.11.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}

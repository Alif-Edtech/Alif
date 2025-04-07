#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2024 Alif Edtech
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

"""
Test script for Groq integration with Alif.
This script tests the Groq LLM integration by sending a simple query.
"""

import os
import sys
from config.config import get_learnhouse_config
from src.services.ai.init import get_llm

def test_groq_integration():
    """Test Groq integration by sending a simple query."""
    # Get configuration
    config = get_learnhouse_config()

    # Check if Groq API key is set
    groq_api_key = getattr(config.ai_config, 'groq_api_key', None)
    if not groq_api_key:
        print("Error: Groq API key is not set in the configuration.")
        print("Please set the LEARNHOUSE_GROQ_API_KEY environment variable or update the config.yaml file.")
        return False

    # Check if LLM provider is set to Groq
    llm_provider = getattr(config.ai_config, 'llm_provider', None)
    if llm_provider != 'groq':
        print(f"Warning: LLM provider is set to '{llm_provider}', not 'groq'.")
        print("The test will continue, but it may use a different provider.")

    # Get the default LLM model
    default_model = getattr(config.ai_config, 'default_llm_model', 'meta-llama/llama-4-scout-17b-16e-instruct')
    print(f"Using model: {default_model}")

    # Initialize the LLM
    llm = get_llm(default_model)
    if not llm:
        print("Error: Failed to initialize the LLM.")
        return False

    # Test the LLM with a simple query
    try:
        print("Sending test query to Groq...")
        response = llm.invoke("What is the capital of France?")
        print("\nResponse from Groq:")
        print(response.content)
        print("\nGroq integration test successful!")
        return True
    except Exception as e:
        print(f"Error: Failed to get response from Groq: {e}")
        return False

if __name__ == "__main__":
    success = test_groq_integration()
    sys.exit(0 if success else 1)

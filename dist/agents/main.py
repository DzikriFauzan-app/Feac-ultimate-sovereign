#!/usr/bin/env python3
"""
NeoEngine - Standalone backend entrypoint
"""
from core.engine import NeoEngine

if __name__ == "__main__":
    engine = NeoEngine()
    engine.run()

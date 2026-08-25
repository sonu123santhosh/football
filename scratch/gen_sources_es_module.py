"""
Export data/sources.json as an ES module in js/sources.js for zero-latency client use.
"""

import json

with open(r"c:\Users\LENOVO\Desktop\web\data\sources.json", "r", encoding="utf-8") as f:
    data = json.load(f)

js_content = f"""/**
 * BLUEGUN — Master Source & Attribution Registry (ES Module)
 * Generated from data/sources.json
 */

export const AUDIT_METADATA = {json.dumps(data.get('audit_metadata', {}), indent=2)};

export const SOURCES_REGISTRY = {json.dumps(data.get('sources', []), indent=2)};

export function getSourceById(sourceId) {{
  return SOURCES_REGISTRY.find(s => s.id === sourceId) || null;
}}

export function getSourcesByCategory(category) {{
  if (!category || category === 'ALL') return SOURCES_REGISTRY;
  return SOURCES_REGISTRY.filter(s => s.category.toUpperCase().includes(category.toUpperCase()) || s.type.toUpperCase() === category.toUpperCase());
}}
"""

with open(r"c:\Users\LENOVO\Desktop\web\js\sources.js", "w", encoding="utf-8") as f:
    f.write(js_content.strip())

print("Successfully generated js/sources.js with", len(data.get('sources', [])), "sources!")

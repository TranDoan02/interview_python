from graphviz import Digraph

# Tạo mindmap cho SOLID -> Design Patterns
dot = Digraph("SOLID_to_DesignPatterns", format="png")
dot.attr(rankdir="LR", size="10")

# Node chính
dot.node("SOLID", shape="ellipse", style="filled", color="lightblue", fontsize="18")

# Các nguyên tắc SOLID
principles = {
    "SRP": "Single Responsibility",
    "OCP": "Open/Closed",
    "LSP": "Liskov Substitution",
    "ISP": "Interface Segregation",
    "DIP": "Dependency Inversion"
}

patterns = {
    "SRP": ["Facade", "Mediator", "Repository/Service Layer"],
    "OCP": ["Strategy", "Decorator", "Factory Method", "Observer"],
    "LSP": ["Template Method", "Factory Method", "Composite"],
    "ISP": ["Adapter", "Proxy", "Builder"],
    "DIP": ["Dependency Injection", "Abstract Factory", "Strategy", "Observer"]
}

# Vẽ các node cho SOLID
for key, label in principles.items():
    dot.node(key, label, shape="box", style="rounded,filled", color="lightyellow")
    dot.edge("SOLID", key)

    # Vẽ các pattern liên quan
    for p in patterns[key]:
        pname = f"{key}_{p}"
        dot.node(pname, p, shape="note", style="filled", color="lightgrey")
        dot.edge(key, pname)

# Lưu hình
output_path = "/mnt/data/solid_design_patterns_mindmap"
dot.render(output_path, cleanup=True)

output_path + ".png"

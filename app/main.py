from app.character.fighters import knights
from app.character.character_builds import apply_upgrades


def battle(knights: dict) -> None:
    # Apply upgrades to all knights
    for knight in knights.values():
        apply_upgrades(knight)

    # -------------------------------------------------------------------------------
    # BATTLE:
    lancelot = knights["lancelot"]
    mordred = knights["mordred"]
    red_knight = knights["red_knight"]
    arthur = knights["arthur"]

    # 1 Lancelot vs Mordred:
    lancelot["hp"] -= max(0, mordred["power"] - lancelot["protection"])
    mordred["hp"] -= max(0, lancelot["power"] - mordred["protection"])

    # 2 Arthur vs Red Knight:
    arthur["hp"] -= max(0, red_knight["power"] - arthur["protection"])
    red_knight["hp"] -= max(0, arthur["power"] - red_knight["protection"])

    # Clamp HP to zero
    for knight in [lancelot, mordred, arthur, red_knight]:
        knight["hp"] = max(0, knight["hp"])

    # Return battle results:
    return {
        lancelot["name"]: lancelot["hp"],
        arthur["name"]: arthur["hp"],
        mordred["name"]: mordred["hp"],
        red_knight["name"]: red_knight["hp"],
    }


print(battle(knights))

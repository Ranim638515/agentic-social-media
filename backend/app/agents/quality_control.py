from app.state import PostState


def quality_control(state: PostState) -> dict:
    """Agent 7 (Emna) : controle la qualite et decide accept/revise."""
    # TODO : implementer l'agent (appel LLM, sortie structuree)
    return {"quality_report": {}, "decision": "accept"}

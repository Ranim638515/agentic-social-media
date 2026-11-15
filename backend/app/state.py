from typing import TypedDict, Optional


class PostState(TypedDict, total=False):
    """Etat partage entre tous les agents (brouillon a valider ensemble)."""

    # Entree
    tenant_id: str
    campaign_goal: str

    # Ranim
    brand_profile: dict
    research_report: dict
    content_plan: dict
    post_draft: dict

    # Emna
    visual_asset: dict
    quality_report: dict
    decision: str  # "accept" ou "revise"
    publication_results: dict
    analytics_report: dict
    recommendations: dict

    # Validation humaine (ensemble)
    approval_status: str  # "approved", "edited", "revision", "rejected"
    approved_version: Optional[int]

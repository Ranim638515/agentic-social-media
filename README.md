# Agentic AI for Social Media Management

Equipe : Ranim & Emna

## Lancer le projet
1. Copier `.env.example` vers `.env` et remplir les valeurs
2. `docker compose up -d`
3. `cd backend`, creer et activer un venv, puis `pip install -r requirements.txt`
4. `uvicorn app.main:app --reload`
5. Ouvrir http://localhost:8000/health puis http://localhost:8000/docs

## Repartition des agents
- Ranim : business_understanding, research, strategy, content_generation, seo_optimization
- Emna : visual_generation, quality_control, publishing, analytics, learning
- Ensemble : orchestrateur LangGraph, validation humaine, auth multi-tenant, PostState (backend/app/state.py)

## Git
- Branches : main / dev / feature-*  (ex. feature/agent-strategy, feature/agent-visual)
- Ne jamais commiter le fichier .env

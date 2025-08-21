# CodePro Mark1

CodePro Mark1 is a minimal self-bootstrapping AI builder. It demonstrates a
workflow where autonomous agents plan, implement, and review changes to a
codebase.

## Features
- FastAPI backend providing health and task endpoints.
- React + TypeScript console UI for interacting with the API.
- Git-based agents that plan, code, review, and merge.
- Unit tests covering core endpoints.

## Architecture
```mermaid
flowchart LR
    Frontend -->|REST| Backend
    Backend -->|GitOps| Agents
```

## Prerequisites
- Python 3.11
- Node.js 20
- npm or yarn

## Installation
```bash
git clone <repo>
cd codepro_mark1
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cp .env.sample .env  # populate values
cd frontend && npm install
```

## Running
Start the backend:
```bash
uvicorn backend.main:app --reload
```

Start the frontend in another terminal:
```bash
cd frontend
npm run dev
```

Visit `http://localhost:5173` and add tasks.

## API
| Method | Path   | Description       |
|--------|--------|------------------|
| GET    | /health| Health check     |
| GET    | /tasks | List tasks       |
| POST   | /tasks | Create a task    |

See [backend/README.md](backend/README.md) for details.

## Development Workflow
Run tests with:
```bash
pytest
```

Use `OPENAI_RUN_SEED` to seed deterministic operations where applicable.

## Contributing
1. Fork and branch from `main`.
2. Run tests and ensure checks pass.
3. Submit a pull request.

## Support
Open an issue for bugs or questions.

## License
MIT

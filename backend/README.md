# Backend

The backend is a FastAPI application exposing health and task endpoints.

## Running

```bash
uvicorn backend.main:app --reload
```

The server listens on `http://localhost:8000`.

## API

### `GET /health`
Returns `{"ok": true}` when the service is available.

### `GET /tasks`
Returns the list of in-memory tasks.

### `POST /tasks`
Accepts JSON `{ "id": int, "text": str }` and stores the task.

Tasks are stored in memory and cleared when the process exits.

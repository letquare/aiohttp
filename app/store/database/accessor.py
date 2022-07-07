from app.api.models import InfoAboutDevice, Users
from app.store.database.models import db


class PostgresAccessor:
    def __init__(self):

        self.info = InfoAboutDevice
        self.users = Users
        self.db = None

    def setup(self, application):
        application.on_startup.append(self._on_connect)
        application.on_cleanup.append(self._on_disconnect)

    async def _on_connect(self, application):

        self.config = application["config"]["postgres"]
        await db.set_bind(self.config["database_url"])
        self.db = db

    async def _on_disconnect(self, _):
        if self.db is not None:
            await self.db.pop_bind().close()

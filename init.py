import asyncio
from server import OriginChatsServer
from logger import Logger

async def main():
    """Main function to start the SaltyChats server"""
    Logger.info("Initializing SaltyChats server...")
    server = OriginChatsServer()
    Logger.success("Server initialized successfully")
    await server.start_server()

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        Logger.warning("Server stopped by user")
    except Exception as e:
        Logger.error(f"Server error: {str(e)}")

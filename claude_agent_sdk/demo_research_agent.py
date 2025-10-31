"""
Demo of the Research Agent - Live Example
This demonstrates the core capabilities of the Claude Agent SDK
"""

import asyncio
from research_agent.agent import send_query


async def main():
    print("\n" + "=" * 60)
    print("🚀 RESEARCH AGENT DEMO")
    print("=" * 60 + "\n")

    # Example 1: Simple one-off query
    print("📌 EXAMPLE 1: Simple Research Query")
    print("-" * 60)
    result1 = await send_query(
        "What is the Claude Agent SDK? Do one websearch and be concise (2-3 sentences)."
    )
    print(f"\n✅ Result:\n{result1}\n")

    print("\n" + "=" * 60 + "\n")

    # Example 2: Multi-turn conversation with context
    print("📌 EXAMPLE 2: Multi-Turn Conversation (Context Retention)")
    print("-" * 60)

    # First query
    print("🔍 First query: Learning about Anthropic...")
    result2a = await send_query(
        "What is Anthropic? Do one websearch and give me 2-3 key points.",
        continue_conversation=False,  # Start new conversation
    )
    print(f"\n✅ Result:\n{result2a}\n")

    # Follow-up query using the same context
    print("\n🔍 Follow-up query: Asking about their products...")
    result2b = await send_query(
        "What are their main products? Be concise.",
        continue_conversation=True,  # Continue the previous conversation
    )
    print(f"\n✅ Result:\n{result2b}\n")

    print("\n" + "=" * 60)
    print("✨ Demo Complete!")
    print("=" * 60 + "\n")


if __name__ == "__main__":
    asyncio.run(main())

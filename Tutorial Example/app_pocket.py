from flow import create_article_flow

def run_flow(topic="AI Safety"):
    """
    Run the article writing workflow with a specific topic
    
    Args:
        topic (str): The topic for the article
    """
    # Initialize shared data with the topic
    shared = {"topic": topic, 'final_output': ''}
    response = ''
    
    # Print starting message
    try:
        response = ''.join([response, f"\n=== Starting Article Workflow on Topic: {topic['content']} ===\n"])
    except:
        response = ''.join([response, f"\n=== Starting Article Workflow on Topic: {topic} ===\n"])

    # Run the flow
    flow = create_article_flow()
    flow.run(shared)
    
    # Output summary
    response = '\n'.join([response, shared['final_output'], "\n=== Workflow Completed ===\n"])
    try:
        response = ''.join([response, f"\n\nTopic: {topic['content']}"])
    except:
        response = ''.join([response, f"\n\nTopic: {topic}"])
    response = ''.join([response, f"\n\nOutline Length: {len(shared['outline'])} characters"])
    response = ''.join([response, f"\n\nDraft Length: {len(shared['draft'])} characters"])
    response = ''.join([response, f"\n\nFinal Article Length: {len(shared['final_article'])} characters"])
    
    output = {"response": response}
    return output

if __name__ == "__main__":
    import sys
    
    # Get topic from command line if provided
    topic = "AI Safety"  # Default topic
    if len(sys.argv) > 1:
        topic = " ".join(sys.argv[1:])
    
    response = run_flow(topic)
    print(output["response"])
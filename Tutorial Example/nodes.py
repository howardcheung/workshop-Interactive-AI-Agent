import re
from pocketflow import Node, BatchNode
from utils.call_llm import call_llm
import yaml

class GenerateOutline(Node):
    def prep(self, shared):
        return shared["topic"]
    
    def exec(self, topic):
        prompt = f"""
Create a simple outline for an article about {topic}.
Include at most 3 main sections (no subsections and no description for sections and subsections).

Output the sections in YAML format as shown below (keep the - and | characters in the output, and no other alternative suggestions):

```yaml
sections:
    - |
        First section 
    - |
        Second section
    - |
        Third section
```"""
        # the llm may output incorrect format for up to 10 times. Use some attempts before successful outputs
        attempts = 0
        max_attempts = 10
        while attempts < max_attempts:
            try:
                response = call_llm(prompt)
                print("Check YAML output:\n", response)
                try:
                    yaml_str = response.split("```yaml")[1].split("```")[0].strip()
                except Exception as e:
                    print(f"Moving with error at {e}")
                    yaml_str = response.split("```yaml")[1].split("```")[0]
            except Exception as e:
                print(f"Repeating with error at {e}")
            finally:
                attempts += 1
            
        structured_result = yaml.safe_load(yaml_str)
        return structured_result
    
    def post(self, shared, prep_res, exec_res):
        # Store the structured data
        shared["outline_yaml"] = exec_res
        
        # Extract sections
        sections = exec_res["sections"]
        shared["sections"] = sections
        
        # Format for display
        formatted_outline = "\n".join([f"{i+1}. {section}" for i, section in enumerate(sections)])
        shared["outline"] = formatted_outline
        
        # Display the results
        print("\n===== OUTLINE (YAML) =====\n")
        print(yaml.dump(exec_res, default_flow_style=False))
        print("\n===== PARSED OUTLINE =====\n")
        print(formatted_outline)
        print("\n=========================\n")
        
        # put it in share
        shared["final_output"] = ''
        shared["final_output"] = '\n'.join([
            "\n===== PARSED OUTLINE =====\n",
            formatted_outline,
            "\n=========================\n"
        ])
        
        return "default"

class WriteSimpleContent(BatchNode):
    def prep(self, shared):
        # Get the list of sections to process and store for progress tracking
        self.sections = shared.get("sections", [])
        return self.sections
    
    def exec(self, section):
        prompt = f"""
Write a short paragraph (MAXIMUM 100 WORDS) about this section:

{section}

Requirements:
- Explain the idea in simple, easy-to-understand terms
- Use everyday language, avoiding jargon
- Keep it very concise (no more than 100 words)
- Include one brief example or analogy
"""
        content = call_llm(prompt)
        
        # Show progress for this section
        current_section_index = self.sections.index(section) if section in self.sections else 0
        total_sections = len(self.sections)
        print(f"✓ Completed section {current_section_index + 1}/{total_sections}: {section}")
        
        return section, content
    
    def post(self, shared, prep_res, exec_res_list):
        # exec_res_list contains [(section, content), (section, content), ...]
        section_contents = {}
        all_sections_content = []
        
        for section, content in exec_res_list:
            section_contents[section] = content
            all_sections_content.append(f"## {section}\n\n{content}\n")
        
        draft = "\n".join(all_sections_content)
        
        # Store the section contents and draft
        shared["section_contents"] = section_contents
        shared["draft"] = draft
        
        print("\n===== SECTION CONTENTS =====\n")
        for section, content in section_contents.items():
            print(f"### {section}\n")
            print(content)
            print()
        print("===========================\n")
        
        # put it in share
        shared["final_output"] = '\n'.join([
            shared["final_output"],
            "\n===== SECTION CONTENTS =====\n",
        ])
        for section, content in section_contents.items():            
            shared["final_output"] = '\n'.join([
                shared["final_output"],
                f"### {section}\n", content, ''
            ])
        shared["final_output"] = '\n'.join([
            shared["final_output"],
            "\n=========================\n"
        ])
        
        return "default"

class ApplyStyle(Node):
    def prep(self, shared):
        """
        Get the draft from shared data
        """
        return shared["draft"]
    
    def exec(self, draft):
        """
        Apply a specific style to the article
        """
        prompt = f"""
        Rewrite the following draft in a conversational, engaging style. Do not modify any section headings:
        
        {draft}
        
        Make it:
        - Conversational and warm in tone
        - Include rhetorical questions that engage the reader
        - Add analogies and metaphors where appropriate
        - Include a strong opening and conclusion
        """
        return call_llm(prompt)
    
    def post(self, shared, prep_res, exec_res):
        """
        Store the final article in shared data
        """
        shared["final_article"] = exec_res
        print("\n===== FINAL ARTICLE =====\n")
        print(exec_res)
        print("\n========================\n")
        
        # put it in share
        shared["final_output"] = '\n'.join([
            shared["final_output"],
            "\n===== FINAL ARTICLE =====\n",
            exec_res,
            "\n========================\n"
        ])
        return "default" 
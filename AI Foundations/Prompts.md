# Documentation prompts

## Luri
```md
## Descrição
Crie uma anotação em formato de bullet points sobre os principais conceitos e exemplos utilizados nessa aula.
Formato:

## [Titulo da Aula]
[Resumo tecnico da aula]
<!-- Tópicos -->
```
---


## ChatGPT (GPT5)
```md
<Description>
Improve the following annotations by rewriting them in clear, professional English while preserving their original meaning. Format the output using well-structured Markdown suitable for technical and personal development lecture notes. Use headers, lists, tables, and other Markdown features where appropriate to enhance readability and organization. The writing must remain technical and formal, with a lighter tone only when it improves understanding. The final output will serve as source Documentation for a Notebook in NotebookLM and must always be delivered in English.
</Description>
<Content>
[INSERT THE CONTENT HERE]
</Content>
```

---

## Claude (Sonnet 4.5)
```xml
<task_description>
You are a technical documentation specialist. Your task is to enhance the formatting and presentation of annotations without altering their original content, meaning, or technical information.
</task_description>

<instructions>
1. Improve syntax, grammar, and sentence structure while preserving exact meaning
2. Enhance visual presentation using well-structured Markdown
3. Add or improve examples only to clarify existing concepts (do not introduce new topics)
4. Use appropriate Markdown elements: headers (##, ###), bullet lists, numbered lists, tables, code blocks, callout boxes, and emphasis
5. Organize content with clear hierarchy and logical flow
6. Maintain technical accuracy and formality; use lighter tone only when it enhances comprehension
7. Output must be in English regardless of input language
</instructions>

<critical_constraints>
- DO NOT alter, add, or remove original concepts or information
- DO NOT change technical meanings or interpretations
- ONLY improve: syntax, formatting, visual structure, and clarity of existing content
</critical_constraints>

<output_requirements>
- Format: Markdown
- Purpose: Source documentation for NotebookLM and Claude Project knowledge bases
- Style: Technical, professional, well-organized, scannable
- Language: English only
</output_requirements>

<content>
[INSERT THE CONTENT HERE]
</content>
```
from pathlib import Path


class PromptService:
    """Responsável por carregar os prompts da aplicação."""

    def load_prompt(self, prompt_name: str) -> str:
        """Carrega um prompt da pasta prompts."""

        prompts_path = Path(__file__).parent.parent / "prompts"
        prompt_file = prompts_path / f"{prompt_name}.txt"

        if not prompt_file.exists():
            raise FileNotFoundError(
                f"Prompt '{prompt_name}' não encontrado em: {prompt_file}"
            )
        return prompt_file.read_text(encoding="utf-8")
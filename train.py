import os
import sys
from transformers import GPT2LMHeadModel, GPT2TokenizerFast, TextDataset, DataCollatorForLanguageModeling, Trainer, TrainingArguments

def main():
    model_name = "mrm8488/spanish-gpt2"
    try:
        # Cargar tokenizador y modelo base
        tokenizer = GPT2TokenizerFast.from_pretrained(model_name)
        model = GPT2LMHeadModel.from_pretrained(model_name)
    except Exception as e:
        sys.exit(f"Error al cargar el modelo base '{model_name}': {e}")
    
    def load_dataset(train_file, tokenizer, block_size=128):
        return TextDataset(
            tokenizer=tokenizer,
            file_path=train_file,
            block_size=block_size,
            overwrite_cache=True,
        )
    
    train_file = "corpus.txt"
    if not os.path.exists(train_file):
        sys.exit("Error: No se encontró 'corpus.txt' en la raíz del proyecto.")
    
    try:
        dataset = load_dataset(train_file, tokenizer)
    except Exception as e:
        sys.exit(f"Error al cargar el dataset desde '{train_file}': {e}")
    
    data_collator = DataCollatorForLanguageModeling(tokenizer=tokenizer, mlm=False)
    
    training_args = TrainingArguments(
        output_dir="./finetuned-model",
        overwrite_output_dir=True,
        num_train_epochs=3,
        per_device_train_batch_size=2,
        save_steps=500,
        save_total_limit=2,
        logging_steps=100,
        learning_rate=5e-5,
    )
    
    trainer = Trainer(
        model=model,
        args=training_args,
        data_collator=data_collator,
        train_dataset=dataset,
    )
    
    try:
        trainer.train()
    except Exception as e:
        sys.exit(f"Error durante el entrenamiento: {e}")
    
    try:
        trainer.save_model("./finetuned-model")
        tokenizer.save_pretrained("./finetuned-model")
        print("Modelo finetuneado y tokenizador guardados en './finetuned-model'")
    except Exception as e:
        sys.exit(f"Error al guardar el modelo finetuneado: {e}")

if __name__ == "__main__":
    main()

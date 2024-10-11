from PIL import Image, ImageDraw, ImageFont
import os


base_image_path = r'Static\ass.png'  
output_dir = r'Static\output'          

os.makedirs(output_dir, exist_ok=True)


def generate(name, sector, email):
    filename = f"{name}_{sector}.png"
    output_image_path = os.path.join(output_dir, filename)

    try:
        
        if not os.path.exists(base_image_path):
            print(f"Erro: A imagem base '{base_image_path}' não foi encontrada.")
            raise FileNotFoundError(f"A imagem base '{base_image_path}' não foi encontrada.")

        
        print(f"Abrindo a imagem base: {base_image_path}")
        base_image = Image.open(base_image_path)
        draw = ImageDraw.Draw(base_image)

        
        font_path1 = 'generate_img/fonts/RethinkSans-Bold.ttf'
        font_path2 = 'generate_img/fonts/RethinkSans-VariableFont_wght.ttf'

        print("Verificando se as fontes existem...")
        if not os.path.exists(font_path1):
            print(f"Erro: Fonte '{font_path1}' não encontrada.")
        if not os.path.exists(font_path2):
            print(f"Erro: Fonte '{font_path2}' não encontrada.")

        if not os.path.exists(font_path1) or not os.path.exists(font_path2):
            raise FileNotFoundError("Fontes não encontradas. Verifique os caminhos para as fontes.")

        
        email_font_size = 19
        email_color = (37, 35, 122)  
        email_position = (81, 209)  
        email_font = ImageFont.truetype(font_path2, email_font_size)
        print(f"Desenhando o e-mail '{email}' na posição {email_position}")
        draw.text(email_position, email, fill=email_color, font=email_font)

       
        name_font_size = 40  
        name_color = (37, 35, 122)  
        name_position = (50, 35)  
        name_font = ImageFont.truetype(font_path1, name_font_size)
        print(f"Desenhando o nome '{name}' na posição {name_position}")
        draw.text(name_position, name, fill=name_color, font=name_font)

        
        sector_font_size = 23  
        sector_color = (37, 35, 122) 
        sector_position = (55, 90) 
        sector_font = ImageFont.truetype(font_path2, sector_font_size)
        print(f"Desenhando o setor '{sector}' na posição {sector_position}")
        draw.text(sector_position, sector, fill=sector_color, font=sector_font)

        
        print(f"Salvando a imagem gerada em: {output_image_path}")
        base_image.save(output_image_path)

        print("Imagem gerada com sucesso.")
        
        
        image_url = f"/static/output/{filename.replace(' ', '%20')}"

       
        return {"message": "Image generated successfully", "imageUrl": image_url}, 200


    except Exception as e:
        print(f"Erro ao gerar a imagem: {e}")
        return {"error": str(e)}, 500


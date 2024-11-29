suspenso = """
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CNPJs Suspensos</title>
</head>
<body style="font-family: Arial, sans-serif; background-color: #ffffff; margin: 0; padding: 0; color: #333;">
    <div style="max-width: 600px; margin: 20px auto; background: #f9f9f9; border: 1px solid #ddd; border-radius: 10px; overflow: hidden; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);">
        <div style="background-color: #000000; color: white; text-align: center; padding: 20px; font-size: 1.5em;">
            CNPJs Suspensos
        </div>
        <div style="padding: 20px;">
            <p style="margin-bottom: 15px; text-align: justify;">
                Prezado(a) <strong>{client_name}</strong>,
            </p>
            <p style="margin-bottom: 15px; text-align: justify;">
                A Receita Federal <strong>SUSPENDEU O CNPJ</strong> de 7,2 milhões de Microempreendedores Individuais em todo o Brasil apenas em 2024 — e um deles é você.
            </p>
            <p style="margin-bottom: 15px; text-align: justify;">
                ⚠ <strong>Atenção:</strong> A exclusão do regime MEI implica no pagamento de mais impostos, custos com contador e uma série de outras obrigações que, se não regularizadas, podem afetar diretamente seu CPF como sócio.
            </p>
            <p style="margin-bottom: 15px; text-align: justify;">
                <strong>Mas como regularizar sua situação agora?</strong>
            </p>
            <p style="margin-bottom: 15px; text-align: justify;">
                Acesse o Portal do MEI, faça o preenchimento e envio da <strong>Declaração Anual do Simples Nacional-MEI</strong>, informando dados da atividade econômica exercida, faturamento, existência de funcionários e outras informações cadastrais.
            </p>
            <p style="margin-bottom: 15px; text-align: justify;">
                Simples, não? Mas para empreendedores como você, o tempo vale o dobro... E nós sabemos disso.
            </p>
            <p style="margin-bottom: 15px; text-align: justify;">
                Entre em contato pelo WhatsApp com nossos especialistas da <strong>MBK MEI</strong>, o braço da MBK - Grupo de Serviços Empresariais focado em otimizar resultados de microempreendedores em <strong>{client_city}</strong>.
            </p>
            <p style="margin-bottom: 15px; text-align: justify;">
                Evite complicações: simplifique com a <strong>MBK MEI</strong> e dedique seu tempo ao que realmente importa para o seu negócio.
            </p>
            <div style="text-align: center; margin: 20px 0;">
                <a href="https://wa.me/554184443380" target="_blank" style="background-color: #c3222a; color: white; text-decoration: none; padding: 15px 25px; border-radius: 5px; font-weight: bold; display: inline-block;">
                    👉 Quero regularizar meu MEI
                </a>
            </div>
        </div>
        <div style="background-color: #ffffff; text-align: center; padding: 20px; font-size: 0.9em; color: #777;">
            <p style="margin: 5px 0;">
                <strong>Bruno Fey</strong><br>Diretor - MBK Contabilidade
            </p>
            <p style="margin: 5px 0;">"Simplificando processos burocráticos há 30 anos."</p>
            <p style="margin: 5px 0;">Tel: <a href="tel:+5541984443380" style="color: #0056b3; text-decoration: none;">(41) 98444-3380</a></p>
            <p style="margin: 5px 0;">E-mail: <a href="mailto:contato@mbkcontabilidade.com" style="color: #0056b3; text-decoration: none;">contato@mbkcontabilidade.com</a></p>
            <p>
                <img src="https://ci3.googleusercontent.com/mail-sig/AIorK4wH-bUT5TfOrAlZ5z6Qv74MLUwFzmsShtYX7Zw4HuIUWWqn2QushlYpXeySgH_Wx1qoMwv-irw" alt="MBK Logo" width="200" style="margin-top: 10px;">
            </p>
            <p style="background-color: #ffffff; padding: 10px; font-size: 0.8em; font-style: italic; border-radius: 5px;">
                Este e-mail é confidencial e destinado apenas ao destinatário. Caso tenha recebido por engano, notifique-nos imediatamente e exclua a mensagem.
            </p>
        </div>
    </div>
</body>
</html>

"""


inapto = """
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Notificação de CNPJ Inapto</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            color: #333;
            line-height: 1.6;
            background-color: #ffffff;
            padding: 0;
            margin: 0;
        }}
        .container {{
            max-width: 600px;
            margin: 20px auto;
            background: #f9f9f9;
            border: 1px solid #ddd;
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            overflow: hidden;
        }}
        .header {{
            background-color: #000000;
            color: white;
            text-align: center;
            padding: 20px;
            font-size: 1.5em;
        }}
        .content {{
            padding: 20px;
        }}
        .content p {{
            margin-bottom: 15px;
            text-align: justify;
        }}
        .content ul {{
            margin-left: 20px;
            list-style-type: disc;
        }}
        .cta {{
            text-align: center;
            margin: 20px 0;
        }}
        .cta a {{
            background-color: #c3222a;
            color: white;
            text-decoration: none;
            padding: 10px 20px;
            border-radius: 5px;
            font-weight: bold;
        }}
        .cta a:hover {{
            background-color: #c3222a;
        }}
        .footer {{
            background-color: #ffffff;
            text-align: center;
            padding: 20px;
            font-size: 0.9em;
            color: #777;
        }}
        .footer p {{
            margin: 5px 0;
        }}
        .footer a {{
            color: #0056b3;
            text-decoration: none;
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            CNPJs INAPTOS
        </div>
        <div class="content">
            <p>Prezado(a) <strong>[NOME EMPRESA]</strong>,</p>
            <p>
                A Receita Federal informou que cerca de <strong>1,1 milhões de Microempreendedores Individuais</strong> em todo o Brasil <strong>PAGARÃO MAIS IMPOSTOS EM 2025</strong> — e um deles é você.
            </p>
            <p>
                ⚠ <strong>Atenção:</strong> Por não cumprimento de obrigações acessórias, a partir de <strong>01/01/2025</strong> você pode ser excluído do MEI, o que implica em:
            </p>
            <ul>
                <li>Maior gasto com impostos, por pagar sobre o quanto você ganha todo mês;</li>
                <li>Contratar um contador;</li>
                <li>Contratação de um sistema de emissão de notas fiscais;</li>
                <li>Entre outros novos custos…</li>
            </ul>
            <p>
                Então, você precisa regularizar sua empresa agora. E nós te dizemos como.
            </p>
            <p>
                Acesse o Portal do MEI, faça o preenchimento e envio da <strong>Declaração Anual do Simples Nacional-MEI</strong>, informando dados da atividade econômica exercida, faturamento, existência de funcionários e outras informações cadastrais dos últimos dois anos.
            </p>
            <p>
                Simples, não? Mas empreendedores como você não têm apenas isso a fazer, já que seu tempo vale o dobro...
            </p>
            <p>
                Por isso, nós queremos te ajudar a regularizar seu MEI.
            </p>
            <p>
                Para ter a empresa totalmente regularizada sem dor de cabeça, entre em contato pelo WhatsApp com nossos especialistas da <strong>MBK MEI</strong>, o braço da MBK - Grupo de Serviços Empresariais focado em otimizar resultados de microempreendedores em <strong>[NOME DA CIDADE]</strong>.
            </p>
            <p>
                Evite complicações: simplifique com a <strong>MBK MEI</strong> e dedique seu tempo ao que realmente importa para o seu negócio.
            </p>
            <div class="cta">
                <a href="https://wa.me/554184443380" target="_blank">👉 Não quero perder meu MEI</a>
            </div>
        </div>
        <div class="footer">
            <p><strong>Bruno Fey</strong><br>Diretor - MBK Contabilidade</p>
            <p>"Simplificando processos burocráticos há 30 anos."</p>
            <p>Tel: <a href="tel:+5541984443380">(41) 98444-3380</a></p>
            <p>E-mail: <a href="mailto:contato@mbkcontabilidade.com">contato@mbkcontabilidade.com</a></p>
            <p>
                <img src="https://ci3.googleusercontent.com/mail-sig/AIorK4wH-bUT5TfOrAlZ5z6Qv74MLUwFzmsShtYX7Zw4HuIUWWqn2QushlYpXeySgH_Wx1qoMwv-irw" alt="MBK Logo" width="200">
            </p>
            <p style="background-color: #ffffff; padding: 10px; font-size: 0.8em; font-style: italic; border-radius: 5px;">
                Este e-mail é confidencial e destinado apenas ao destinatário. Caso tenha recebido por engano, notifique-nos imediatamente e exclua a mensagem.
            </p>
        </div>
    </div>
</body>
</html>
"""
baixado = """
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Notificação de CNPJ Baixado</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            color: #333;
            line-height: 1.6;
            background-color: #ffffff;
            padding: 0;
            margin: 0;
        }}
        .container {{
            max-width: 600px;
            margin: 20px auto;
            background: #f9f9f9;
            border: 1px solid #ddd;
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            overflow: hidden;
        }}
        .header {{
            background-color: #000000;
            color: white;
            text-align: center;
            padding: 20px;
            font-size: 1.5em;
        }}
        .content {{
            padding: 20px;
        }}
        .content p {{
            margin-bottom: 15px;
            text-align: justify;
        }}
        .content ul {{
            margin-left: 20px;
            list-style-type: disc;
        }}
        .cta {{
            text-align: center;
            margin: 20px 0;
        }}
        .cta a {{
            background-color: #c3222a;
            color: white;
            text-decoration: none;
            padding: 10px 20px;
            border-radius: 5px;
            font-weight: bold;
        }}
        .cta a:hover {{
            background-color: #c3222a;
        }}
        .footer {{
            background-color: #ffffff;
            text-align: center;
            padding: 20px;
            font-size: 0.9em;
            color: #777;
        }}
        .footer p {{
            margin: 5px 0;
        }}
        .footer a {{
            color: #0056b3;
            text-decoration: none;
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            CNPJs BAIXADOS
        </div>
        <div class="content">
            <p>Prezado(a) <strong>[NOME EMPRESA]</strong>,</p>
            <p>
                Você sabe que formalizar suas atividades com um CNPJ é importante. Mas conhece todas as vantagens de ser um MEI?
            </p>
            <p>
                Com os incentivos do governo federal, o MEI pode:
            </p>
            <ul>
                <li>Ganhar direito à aposentadoria;</li>
                <li>Receber auxílio-doença;</li>
                <li>Pagar apenas uma guia mensal de impostos, sem burocracia ou gastos extras;</li>
                <li>Ter acesso a crédito facilitado e mais barato;</li>
                <li>Prestar serviço para empresas com emissão de nota fiscal.</li>
            </ul>
            <p>
                Por isso, se você deseja retornar ao mundo do empreendedorismo, a <strong>MBK MEI</strong> pode abrir seu novo CNPJ gratuitamente.
            </p>
            <p>
                Tem dúvidas fiscais, trabalhistas ou administrativas que te impedem de gerir a empresa? Nós disponibilizamos uma consultoria gratuita por 90 dias para auxiliar você a crescer sem complicações.
            </p>
            <p>
                Abra seu MEI conosco pelo Whatsapp em até 20 minutos e volte a fazer a diferença no seu ramo!
            </p>
            <div class="cta">
                <a href="https://wa.me/554184443380" target="_blank">👉 Quero abrir meu MEI gratuitamente</a>
            </div>
        </div>
        <div class="footer">
            <p><strong>Bruno Fey</strong><br>Diretor - MBK Contabilidade</p>
            <p>"Simplificando processos burocráticos há 30 anos."</p>
            <p>Tel: <a href="tel:+5541984443380">(41) 98444-3380</a></p>
            <p>E-mail: <a href="mailto:contato@mbkcontabilidade.com">contato@mbkcontabilidade.com</a></p>
            <p>
                <img src="https://ci3.googleusercontent.com/mail-sig/AIorK4wH-bUT5TfOrAlZ5z6Qv74MLUwFzmsShtYX7Zw4HuIUWWqn2QushlYpXeySgH_Wx1qoMwv-irw" alt="MBK Logo" width="200">
            </p>
            <p style="background-color: #ffffff; padding: 10px; font-size: 0.8em; font-style: italic; border-radius: 5px;">
                Este e-mail é confidencial e destinado apenas ao destinatário. Caso tenha recebido por engano, notifique-nos imediatamente e exclua a mensagem.
            </p>
        </div>
    </div>
</body>
</html>
"""
ativo = """
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Notificação de CNPJ Ativo</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            color: #333;
            line-height: 1.6;
            background-color: #ffffff;
            padding: 0;
            margin: 0;
        }}
        .container {{
            max-width: 600px;
            margin: 20px auto;
            background: #f9f9f9;
            border: 1px solid #ddd;
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            overflow: hidden;
        }}
        .header {{
            background-color: #000000;
            color: white;
            text-align: center;
            padding: 20px;
            font-size: 1.5em;
        }}
        .content {{
            padding: 20px;
        }}
        .content p {{
            margin-bottom: 15px;
            text-align: justify;
        }}
        .cta {{
            text-align: center;
            margin: 20px 0;
        }}
        .cta a {{
            background-color: #c3222a;
            color: white;
            text-decoration: none;
            padding: 10px 20px;
            border-radius: 5px;
            font-weight: bold;
        }}
        .cta a:hover {{
            background-color: #c3222a;
        }}
        .footer {{
            background-color: #ffffff;
            text-align: center;
            padding: 20px;
            font-size: 0.9em;
            color: #777;
        }}
        .footer p {{
            margin: 5px 0;
        }}
        .footer a {{
            color: #0056b3;
            text-decoration: none;
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            CNPJs ATIVOS
        </div>
        <div class="content">
            <p>Prezado(a) <strong>[NOME EMPRESA]</strong>,</p>
            <p>
                A Receita Federal enviou uma <strong>NOTIFICAÇÃO DE EXCLUSÃO</strong> para 1,1 milhão de Microempreendedores Individuais em todo o Brasil — e um deles é você.
            </p>
            <p>
                ⚠ <strong>Atenção:</strong> A exclusão do regime MEI implica no pagamento de mais impostos, custos com contador e uma série de outras obrigações que, se não regularizadas, podem afetar diretamente seu CPF como sócio.
            </p>
            <p>
                <strong>Mas como regularizar sua situação agora?</strong>
            </p>
            <p>
                Acesse o Portal do MEI, consulte seus débitos com a Receita Federal, faça o preenchimento e envio da <strong>Declaração Anual do Simples Nacional-MEI</strong> e, caso haja dívidas, dê entrada num parcelamento até <strong>01/01/2025</strong>.
            </p>
            <p>
                Simples, não? Mas para empreendedores como você, o tempo vale o dobro... E nós sabemos disso.
            </p>
            <p>
                Por isso, se você quer ter sua empresa regularizada sem dor de cabeça, entre em contato pelo WhatsApp com nossos especialistas da <strong>MBK MEI</strong>, o braço da MBK - Grupo de Serviços Empresariais focado em otimizar resultados de microempreendedores em <strong>[NOME DA CIDADE]</strong>.
            </p>
            <p>
                Evite complicações: simplifique com a <strong>MBK MEI</strong> e dedique seu tempo ao que realmente importa para o seu negócio.
            </p>
            <div class="cta">
                <a href="https://wa.me/554184443380" target="_blank">👉 Quero regularizar meu MEI</a>
            </div>
        </div>
        <div class="footer">
            <p><strong>Bruno Fey</strong><br>Diretor - MBK Contabilidade</p>
            <p>"Simplificando processos burocráticos há 30 anos."</p>
            <p>Tel: <a href="tel:+5541984443380">(41) 98444-3380</a></p>
            <p>E-mail: <a href="mailto:contato@mbkcontabilidade.com">contato@mbkcontabilidade.com</a></p>
            <p>
                <img src="https://ci3.googleusercontent.com/mail-sig/AIorK4wH-bUT5TfOrAlZ5z6Qv74MLUwFzmsShtYX7Zw4HuIUWWqn2QushlYpXeySgH_Wx1qoMwv-irw" alt="MBK Logo" width="200">
            </p>
            <p style="background-color: #ffffff; padding: 10px; font-size: 0.8em; font-style: italic; border-radius: 5px;">
                Este e-mail é confidencial e destinado apenas ao destinatário. Caso tenha recebido por engano, notifique-nos imediatamente e exclua a mensagem.
            </p>
        </div>
    </div>
</body>
</html>
"""
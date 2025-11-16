"""
Sistema de Análise de Comportamento de Clientes - Modelo Probabilístico
=====================================================================

Este módulo implementa um modelo probabilístico para análise de comportamento de clientes
em uma loja online, considerando três variáveis principais:
1. Histórico de compras (purchase_history)
2. Tempo no site (time_on_site)
3. Interação com promoções (promotion_interaction)

O modelo utiliza redes bayesianas e o teorema de Bayes para calcular probabilidades
de compra baseadas nas evidências observadas.
"""

import numpy as np
from typing import Dict, List, Tuple, Optional
from dataclasses import dataclass
from enum import Enum
import matplotlib.pyplot as plt
import seaborn as sns


class PurchaseHistory(Enum):
    """Histórico de compras do cliente"""
    NEW_CUSTOMER = "new_customer"      # Cliente novo (sem compras anteriores)
    OCCASIONAL = "occasional"          # Cliente ocasional (1-3 compras)
    REGULAR = "regular"                # Cliente regular (4-10 compras)
    FREQUENT = "frequent"              # Cliente frequente (10+ compras)


class TimeOnSite(Enum):
    """Tempo gasto no site"""
    SHORT = "short"                    # < 2 minutos
    MEDIUM = "medium"                  # 2-10 minutos
    LONG = "long"                      # > 10 minutos


class PromotionInteraction(Enum):
    """Interação com promoções"""
    NO_CLICK = "no_click"              # Não clicou em promoções
    FEW_CLICKS = "few_clicks"          # 1-2 cliques em promoções
    MANY_CLICKS = "many_clicks"        # 3+ cliques em promoções


@dataclass
class CustomerProfile:
    """Perfil do cliente com suas características observadas"""
    purchase_history: PurchaseHistory
    time_on_site: TimeOnSite
    promotion_interaction: PromotionInteraction
    
    def __str__(self):
        return (f"Cliente: {self.purchase_history.value}, "
                f"Tempo: {self.time_on_site.value}, "
                f"Promoções: {self.promotion_interaction.value}")


class CustomerBehaviorModel:
    """
    Modelo probabilístico para análise de comportamento de clientes.
    
    Este modelo utiliza uma rede bayesiana simples onde:
    - Histórico de compras é uma variável independente
    - Tempo no site e interação com promoções são influenciados pelo histórico
    - A probabilidade de compra é influenciada por todas as três variáveis
    """
    
    def __init__(self):
        """Inicializa o modelo com probabilidades baseadas em dados históricos"""
        self._initialize_probabilities()
    
    def _initialize_probabilities(self):
        """Inicializa as probabilidades condicionais baseadas em dados típicos de e-commerce"""
        
        # Probabilidades a priori para histórico de compras
        self.p_purchase_history = {
            PurchaseHistory.NEW_CUSTOMER: 0.40,    # 40% dos visitantes são novos
            PurchaseHistory.OCCASIONAL: 0.30,      # 30% são ocasionais
            PurchaseHistory.REGULAR: 0.20,         # 20% são regulares
            PurchaseHistory.FREQUENT: 0.10         # 10% são frequentes
        }
        
        # Probabilidades condicionais para tempo no site dado o histórico
        self.p_time_given_history = {
            (PurchaseHistory.NEW_CUSTOMER, TimeOnSite.SHORT): 0.60,
            (PurchaseHistory.NEW_CUSTOMER, TimeOnSite.MEDIUM): 0.30,
            (PurchaseHistory.NEW_CUSTOMER, TimeOnSite.LONG): 0.10,
            
            (PurchaseHistory.OCCASIONAL, TimeOnSite.SHORT): 0.40,
            (PurchaseHistory.OCCASIONAL, TimeOnSite.MEDIUM): 0.45,
            (PurchaseHistory.OCCASIONAL, TimeOnSite.LONG): 0.15,
            
            (PurchaseHistory.REGULAR, TimeOnSite.SHORT): 0.25,
            (PurchaseHistory.REGULAR, TimeOnSite.MEDIUM): 0.50,
            (PurchaseHistory.REGULAR, TimeOnSite.LONG): 0.25,
            
            (PurchaseHistory.FREQUENT, TimeOnSite.SHORT): 0.15,
            (PurchaseHistory.FREQUENT, TimeOnSite.MEDIUM): 0.40,
            (PurchaseHistory.FREQUENT, TimeOnSite.LONG): 0.45
        }
        
        # Probabilidades condicionais para interação com promoções dado o histórico
        self.p_promo_given_history = {
            (PurchaseHistory.NEW_CUSTOMER, PromotionInteraction.NO_CLICK): 0.70,
            (PurchaseHistory.NEW_CUSTOMER, PromotionInteraction.FEW_CLICKS): 0.25,
            (PurchaseHistory.NEW_CUSTOMER, PromotionInteraction.MANY_CLICKS): 0.05,
            
            (PurchaseHistory.OCCASIONAL, PromotionInteraction.NO_CLICK): 0.50,
            (PurchaseHistory.OCCASIONAL, PromotionInteraction.FEW_CLICKS): 0.35,
            (PurchaseHistory.OCCASIONAL, PromotionInteraction.MANY_CLICKS): 0.15,
            
            (PurchaseHistory.REGULAR, PromotionInteraction.NO_CLICK): 0.30,
            (PurchaseHistory.REGULAR, PromotionInteraction.FEW_CLICKS): 0.45,
            (PurchaseHistory.REGULAR, PromotionInteraction.MANY_CLICKS): 0.25,
            
            (PurchaseHistory.FREQUENT, PromotionInteraction.NO_CLICK): 0.20,
            (PurchaseHistory.FREQUENT, PromotionInteraction.FEW_CLICKS): 0.40,
            (PurchaseHistory.FREQUENT, PromotionInteraction.MANY_CLICKS): 0.40
        }
        
        # Probabilidades condicionais para compra dado todas as variáveis
        self.p_purchase_given_all = {
            # (histórico, tempo, promoção) -> probabilidade de compra
            (PurchaseHistory.NEW_CUSTOMER, TimeOnSite.SHORT, PromotionInteraction.NO_CLICK): 0.05,
            (PurchaseHistory.NEW_CUSTOMER, TimeOnSite.SHORT, PromotionInteraction.FEW_CLICKS): 0.12,
            (PurchaseHistory.NEW_CUSTOMER, TimeOnSite.SHORT, PromotionInteraction.MANY_CLICKS): 0.20,
            (PurchaseHistory.NEW_CUSTOMER, TimeOnSite.MEDIUM, PromotionInteraction.NO_CLICK): 0.15,
            (PurchaseHistory.NEW_CUSTOMER, TimeOnSite.MEDIUM, PromotionInteraction.FEW_CLICKS): 0.25,
            (PurchaseHistory.NEW_CUSTOMER, TimeOnSite.MEDIUM, PromotionInteraction.MANY_CLICKS): 0.35,
            (PurchaseHistory.NEW_CUSTOMER, TimeOnSite.LONG, PromotionInteraction.NO_CLICK): 0.25,
            (PurchaseHistory.NEW_CUSTOMER, TimeOnSite.LONG, PromotionInteraction.FEW_CLICKS): 0.40,
            (PurchaseHistory.NEW_CUSTOMER, TimeOnSite.LONG, PromotionInteraction.MANY_CLICKS): 0.55,
            
            (PurchaseHistory.OCCASIONAL, TimeOnSite.SHORT, PromotionInteraction.NO_CLICK): 0.10,
            (PurchaseHistory.OCCASIONAL, TimeOnSite.SHORT, PromotionInteraction.FEW_CLICKS): 0.20,
            (PurchaseHistory.OCCASIONAL, TimeOnSite.SHORT, PromotionInteraction.MANY_CLICKS): 0.30,
            (PurchaseHistory.OCCASIONAL, TimeOnSite.MEDIUM, PromotionInteraction.NO_CLICK): 0.25,
            (PurchaseHistory.OCCASIONAL, TimeOnSite.MEDIUM, PromotionInteraction.FEW_CLICKS): 0.40,
            (PurchaseHistory.OCCASIONAL, TimeOnSite.MEDIUM, PromotionInteraction.MANY_CLICKS): 0.55,
            (PurchaseHistory.OCCASIONAL, TimeOnSite.LONG, PromotionInteraction.NO_CLICK): 0.40,
            (PurchaseHistory.OCCASIONAL, TimeOnSite.LONG, PromotionInteraction.FEW_CLICKS): 0.60,
            (PurchaseHistory.OCCASIONAL, TimeOnSite.LONG, PromotionInteraction.MANY_CLICKS): 0.75,
            
            (PurchaseHistory.REGULAR, TimeOnSite.SHORT, PromotionInteraction.NO_CLICK): 0.20,
            (PurchaseHistory.REGULAR, TimeOnSite.SHORT, PromotionInteraction.FEW_CLICKS): 0.35,
            (PurchaseHistory.REGULAR, TimeOnSite.SHORT, PromotionInteraction.MANY_CLICKS): 0.50,
            (PurchaseHistory.REGULAR, TimeOnSite.MEDIUM, PromotionInteraction.NO_CLICK): 0.45,
            (PurchaseHistory.REGULAR, TimeOnSite.MEDIUM, PromotionInteraction.FEW_CLICKS): 0.65,
            (PurchaseHistory.REGULAR, TimeOnSite.MEDIUM, PromotionInteraction.MANY_CLICKS): 0.80,
            (PurchaseHistory.REGULAR, TimeOnSite.LONG, PromotionInteraction.NO_CLICK): 0.65,
            (PurchaseHistory.REGULAR, TimeOnSite.LONG, PromotionInteraction.FEW_CLICKS): 0.80,
            (PurchaseHistory.REGULAR, TimeOnSite.LONG, PromotionInteraction.MANY_CLICKS): 0.90,
            
            (PurchaseHistory.FREQUENT, TimeOnSite.SHORT, PromotionInteraction.NO_CLICK): 0.35,
            (PurchaseHistory.FREQUENT, TimeOnSite.SHORT, PromotionInteraction.FEW_CLICKS): 0.55,
            (PurchaseHistory.FREQUENT, TimeOnSite.SHORT, PromotionInteraction.MANY_CLICKS): 0.70,
            (PurchaseHistory.FREQUENT, TimeOnSite.MEDIUM, PromotionInteraction.NO_CLICK): 0.65,
            (PurchaseHistory.FREQUENT, TimeOnSite.MEDIUM, PromotionInteraction.FEW_CLICKS): 0.80,
            (PurchaseHistory.FREQUENT, TimeOnSite.MEDIUM, PromotionInteraction.MANY_CLICKS): 0.90,
            (PurchaseHistory.FREQUENT, TimeOnSite.LONG, PromotionInteraction.NO_CLICK): 0.80,
            (PurchaseHistory.FREQUENT, TimeOnSite.LONG, PromotionInteraction.FEW_CLICKS): 0.90,
            (PurchaseHistory.FREQUENT, TimeOnSite.LONG, PromotionInteraction.MANY_CLICKS): 0.95
        }
    
    def calculate_purchase_probability(self, customer: CustomerProfile) -> float:
        """
        Calcula a probabilidade de compra para um cliente específico usando o teorema de Bayes.
        
        Args:
            customer: Perfil do cliente com suas características observadas
            
        Returns:
            Probabilidade de compra (0.0 a 1.0)
        """
        # Busca a probabilidade direta na tabela de probabilidades condicionais
        key = (customer.purchase_history, customer.time_on_site, customer.promotion_interaction)
        
        if key in self.p_purchase_given_all:
            return self.p_purchase_given_all[key]
        else:
            # Fallback: calcula usando Bayes se a combinação não estiver na tabela
            return self._calculate_bayesian_probability(customer)
    
    def _calculate_bayesian_probability(self, customer: CustomerProfile) -> float:
        """
        Calcula a probabilidade usando o teorema de Bayes quando não há dados diretos.
        
        P(Compra | Histórico, Tempo, Promoção) = 
        P(Tempo, Promoção | Compra, Histórico) * P(Compra | Histórico) / P(Tempo, Promoção | Histórico)
        """
        # Probabilidade base do histórico
        p_history = self.p_purchase_history[customer.purchase_history]
        
        # Probabilidades condicionais
        p_time_given_history = self.p_time_given_history.get(
            (customer.purchase_history, customer.time_on_site), 0.5
        )
        p_promo_given_history = self.p_promo_given_history.get(
            (customer.purchase_history, customer.promotion_interaction), 0.5
        )
        
        # Estimativa simplificada: assume independência entre tempo e promoção
        # P(Tempo, Promoção | Histórico) ≈ P(Tempo | Histórico) * P(Promoção | Histórico)
        p_evidence_given_history = p_time_given_history * p_promo_given_history
        
        # Probabilidade de compra baseada no histórico (estimativa)
        p_purchase_given_history = {
            PurchaseHistory.NEW_CUSTOMER: 0.20,
            PurchaseHistory.OCCASIONAL: 0.40,
            PurchaseHistory.REGULAR: 0.65,
            PurchaseHistory.FREQUENT: 0.80
        }[customer.purchase_history]
        
        # Aplica o teorema de Bayes
        if p_evidence_given_history > 0:
            # Ajusta a probabilidade baseada nas evidências observadas
            evidence_multiplier = (p_time_given_history * p_promo_given_history) / 0.25  # normalização
            adjusted_probability = min(0.95, p_purchase_given_history * evidence_multiplier)
            return adjusted_probability
        else:
            return p_purchase_given_history
    
    def analyze_customer_segments(self) -> Dict[str, List[Tuple[CustomerProfile, float]]]:
        """
        Analisa diferentes segmentos de clientes e suas probabilidades de compra.
        
        Returns:
            Dicionário com segmentos de clientes e suas probabilidades
        """
        segments = {
            "Alto Potencial": [],
            "Médio Potencial": [],
            "Baixo Potencial": []
        }
        
        # Gera todas as combinações possíveis
        for history in PurchaseHistory:
            for time in TimeOnSite:
                for promo in PromotionInteraction:
                    customer = CustomerProfile(history, time, promo)
                    probability = self.calculate_purchase_probability(customer)
                    
                    if probability >= 0.7:
                        segments["Alto Potencial"].append((customer, probability))
                    elif probability >= 0.4:
                        segments["Médio Potencial"].append((customer, probability))
                    else:
                        segments["Baixo Potencial"].append((customer, probability))
        
        # Ordena por probabilidade decrescente
        for segment in segments:
            segments[segment].sort(key=lambda x: x[1], reverse=True)
        
        return segments
    
    def get_recommendations(self, customer: CustomerProfile) -> List[str]:
        """
        Gera recomendações baseadas no perfil do cliente.
        
        Args:
            customer: Perfil do cliente
            
        Returns:
            Lista de recomendações personalizadas
        """
        probability = self.calculate_purchase_probability(customer)
        recommendations = []
        
        if probability < 0.3:
            recommendations.extend([
                "Exibir promoções mais atrativas na página inicial",
                "Enviar email com desconto especial",
                "Mostrar produtos em destaque",
                "Implementar pop-up com oferta limitada"
            ])
        elif probability < 0.6:
            recommendations.extend([
                "Mostrar produtos relacionados ao histórico",
                "Exibir avaliações de outros clientes",
                "Oferecer frete grátis",
                "Sugerir produtos complementares"
            ])
        else:
            recommendations.extend([
                "Facilitar o processo de checkout",
                "Mostrar produtos premium",
                "Oferecer programa de fidelidade",
                "Exibir produtos em estoque limitado"
            ])
        
        return recommendations
    
    def simulate_customer_scenarios(self, num_scenarios: int = 100) -> Dict[str, float]:
        """
        Simula cenários de clientes para análise estatística.
        
        Args:
            num_scenarios: Número de cenários para simular
            
        Returns:
            Estatísticas dos cenários simulados
        """
        probabilities = []
        
        for _ in range(num_scenarios):
            # Seleciona aleatoriamente um perfil de cliente
            history = np.random.choice(list(PurchaseHistory), 
                                    p=list(self.p_purchase_history.values()))
            time = np.random.choice(list(TimeOnSite))
            promo = np.random.choice(list(PromotionInteraction))
            
            customer = CustomerProfile(history, time, promo)
            prob = self.calculate_purchase_probability(customer)
            probabilities.append(prob)
        
        return {
            "média": np.mean(probabilities),
            "mediana": np.median(probabilities),
            "desvio_padrão": np.std(probabilities),
            "mínimo": np.min(probabilities),
            "máximo": np.max(probabilities),
            "percentil_25": np.percentile(probabilities, 25),
            "percentil_75": np.percentile(probabilities, 75)
        }


def create_visualization(model: CustomerBehaviorModel):
    """
    Cria visualizações do modelo de comportamento de clientes.
    
    Args:
        model: Instância do modelo de comportamento
    """
    # Configuração do estilo
    plt.style.use('seaborn-v0_8')
    fig, axes = plt.subplots(2, 2, figsize=(15, 12))
    fig.suptitle('Análise de Comportamento de Clientes - Modelo Probabilístico', 
                 fontsize=16, fontweight='bold')
    
    # 1. Distribuição de probabilidades por histórico
    histories = list(PurchaseHistory)
    avg_probs = []
    
    for history in histories:
        probs = []
        for time in TimeOnSite:
            for promo in PromotionInteraction:
                customer = CustomerProfile(history, time, promo)
                probs.append(model.calculate_purchase_probability(customer))
        avg_probs.append(np.mean(probs))
    
    axes[0, 0].bar([h.value for h in histories], avg_probs, 
                   color=['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4'])
    axes[0, 0].set_title('Probabilidade Média por Histórico de Compras')
    axes[0, 0].set_ylabel('Probabilidade de Compra')
    axes[0, 0].tick_params(axis='x', rotation=45)
    
    # 2. Heatmap de probabilidades
    heatmap_data = np.zeros((len(TimeOnSite), len(PromotionInteraction)))
    time_labels = [t.value for t in TimeOnSite]
    promo_labels = [p.value for p in PromotionInteraction]
    
    for i, time in enumerate(TimeOnSite):
        for j, promo in enumerate(PromotionInteraction):
            # Usa cliente regular como exemplo
            customer = CustomerProfile(PurchaseHistory.REGULAR, time, promo)
            heatmap_data[i, j] = model.calculate_purchase_probability(customer)
    
    sns.heatmap(heatmap_data, annot=True, fmt='.2f', cmap='YlOrRd',
                xticklabels=promo_labels, yticklabels=time_labels, ax=axes[0, 1])
    axes[0, 1].set_title('Probabilidades: Tempo vs Interação com Promoções\n(Cliente Regular)')
    
    # 3. Distribuição de probabilidades
    all_probs = []
    for history in PurchaseHistory:
        for time in TimeOnSite:
            for promo in PromotionInteraction:
                customer = CustomerProfile(history, time, promo)
                all_probs.append(model.calculate_purchase_probability(customer))
    
    axes[1, 0].hist(all_probs, bins=20, alpha=0.7, color='skyblue', edgecolor='black')
    axes[1, 0].axvline(np.mean(all_probs), color='red', linestyle='--', 
                       label=f'Média: {np.mean(all_probs):.3f}')
    axes[1, 0].set_title('Distribuição de Probabilidades de Compra')
    axes[1, 0].set_xlabel('Probabilidade de Compra')
    axes[1, 0].set_ylabel('Frequência')
    axes[1, 0].legend()
    
    # 4. Segmentação de clientes
    segments = model.analyze_customer_segments()
    segment_sizes = [len(segments[seg]) for seg in segments.keys()]
    segment_labels = list(segments.keys())
    
    colors = ['#FF6B6B', '#FFE66D', '#4ECDC4']
    axes[1, 1].pie(segment_sizes, labels=segment_labels, autopct='%1.1f%%', 
                   colors=colors, startangle=90)
    axes[1, 1].set_title('Distribuição de Segmentos de Clientes')
    
    plt.tight_layout()
    plt.show()


def main():
    """
    Função principal para demonstrar o uso do modelo de comportamento de clientes.
    """
    print("=" * 80)
    print("SISTEMA DE ANÁLISE DE COMPORTAMENTO DE CLIENTES")
    print("Modelo Probabilístico para Loja Online")
    print("=" * 80)
    
    # Cria o modelo
    model = CustomerBehaviorModel()
    
    # Exemplos de clientes
    customers = [
        CustomerProfile(PurchaseHistory.NEW_CUSTOMER, TimeOnSite.SHORT, PromotionInteraction.NO_CLICK),
        CustomerProfile(PurchaseHistory.REGULAR, TimeOnSite.MEDIUM, PromotionInteraction.FEW_CLICKS),
        CustomerProfile(PurchaseHistory.FREQUENT, TimeOnSite.LONG, PromotionInteraction.MANY_CLICKS),
        CustomerProfile(PurchaseHistory.OCCASIONAL, TimeOnSite.LONG, PromotionInteraction.MANY_CLICKS)
    ]
    
    print("\n1. ANÁLISE DE CLIENTES INDIVIDUAIS:")
    print("-" * 50)
    
    for i, customer in enumerate(customers, 1):
        probability = model.calculate_purchase_probability(customer)
        recommendations = model.get_recommendations(customer)
        
        print(f"\nCliente {i}: {customer}")
        print(f"Probabilidade de Compra: {probability:.1%}")
        print("Recomendações:")
        for rec in recommendations[:3]:  # Mostra apenas as 3 primeiras
            print(f"  • {rec}")
    
    print("\n\n2. ANÁLISE DE SEGMENTOS:")
    print("-" * 50)
    
    segments = model.analyze_customer_segments()
    for segment_name, customers_list in segments.items():
        print(f"\n{segment_name} ({len(customers_list)} perfis):")
        for customer, prob in customers_list[:3]:  # Mostra apenas os 3 primeiros
            print(f"  • {customer} - {prob:.1%}")
        if len(customers_list) > 3:
            print(f"  ... e mais {len(customers_list) - 3} perfis")
    
    print("\n\n3. SIMULAÇÃO ESTATÍSTICA:")
    print("-" * 50)
    
    stats = model.simulate_customer_scenarios(1000)
    print("Estatísticas de 1000 cenários simulados:")
    for stat_name, value in stats.items():
        print(f"  {stat_name.replace('_', ' ').title()}: {value:.3f}")
    
    print("\n\n4. INTERPRETAÇÃO DOS RESULTADOS:")
    print("-" * 50)
    print("""
    O modelo probabilístico considera:
    
    • Histórico de Compras: Clientes com histórico mais extenso tendem a ter
      maior probabilidade de compra, refletindo fidelidade e confiança.
    
    • Tempo no Site: Mais tempo navegando indica maior interesse e intenção
      de compra, especialmente quando combinado com interação com promoções.
    
    • Interação com Promoções: Cliques em promoções demonstram engajamento
      e interesse em ofertas, aumentando a probabilidade de conversão.
    
    • Combinações Sinérgicas: O modelo captura como essas variáveis se
      influenciam mutuamente, criando perfis de clientes mais precisos.
    """)
    
    # Cria visualizações
    print("\n5. GERANDO VISUALIZAÇÕES...")
    print("-" * 50)
    try:
        create_visualization(model)
        print("Visualizações criadas com sucesso!")
    except ImportError:
        print("Bibliotecas de visualização não disponíveis. Instale matplotlib e seaborn para ver os gráficos.")
    except Exception as e:
        print(f"Erro ao criar visualizações: {e}")
    
    print("\n" + "=" * 80)
    print("ANÁLISE CONCLUÍDA")
    print("=" * 80)


if __name__ == "__main__":
    main()

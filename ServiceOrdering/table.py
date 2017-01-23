import django_tables2 as tables
from django_tables2.utils import A
from django.utils.safestring import mark_safe
from django.core.urlresolvers import reverse
from .models import Ordem_de_Servico

TEMPLATE = '''
   <a href="{% url 'service:ordem-update' record.id %}"><button type="submit" class="btn btn-default btn-sm">
                            <span class="glyphicon glyphicon-edit"></span>
                    </button></a>
   <form action="{% url 'service:ordem-delete' record.id %}" method="post" style="display: inline">
                        {% csrf_token %}
                        <input type="hidden" name="ordem_id" value="{{ ordem.id }}"/>
                        <button onclick="return confirm('Tem certeza?')" type="submit" class="btn btn-default btn-sm">
                            <span class="glyphicon glyphicon-trash"></span>
                        </button>

                    </form>
'''


class OrdemTable(tables.Table):
    account_number = tables.LinkColumn('data', args=[A('pk')])
    column_name = tables.TemplateColumn(TEMPLATE)

    class Meta:
        model = Ordem_de_Servico

        fields = ['data', 'hora', 'servico', 'empresa', 'contato', 'fone', 'tecnico', 'agencia', 'estado']
        # add class="paleblue" to <table> tag
        attrs = {'class': 'table table-striped'}
        row_attrs = {
            'data-id': lambda record: record.pk
        }
        empty_text = "There are no customers matching the search criteria..."

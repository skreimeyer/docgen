# frozen_string_literal: true

require 'toml-rb'
require 'erb'


class Config
    attr_reader :data

    def initialize(sourcefile)
        @data = TomlRB.load_file(sourcefile)
    end

    def find_or_blank(keys)
        if keys.class.method_defined? :each
            begin
                @data.dig *keys
            rescue
                nil
            end
        if @data[key]

"<div class="row"><div>Project Name and Location: </div><% if project['name'] %><div style="text-decoration:underline"><%= project['name'] %></div><% else %><div class="underline"></div><% end %></div>
"

    def b
        binding
    end
end

config = Config.new('project.toml')

template = File.read('templates/SWPPP_template.erb')
html = ERB.new(template).result config.b

File.open('templates/check.html', 'w') { |f| f.write(html) }

puts 'done'
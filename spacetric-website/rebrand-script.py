#!/usr/bin/env python3
"""
SPACETRIC REBRAND AUTOMATION SCRIPT
====================================

This script automates the complete rebrand from Gadgetronix to Spacetric
across all website files. Use this script to process the remaining HTML files
and complete the comprehensive rebrand.

USAGE:
    python rebrand-script.py [source_directory] [output_directory]

FEATURES:
    - Global find/replace for brand names
    - URL and domain updates
    - Meta tag modifications  
    - Email address updates
    - Content paraphrasing templates
    - File organization
"""

import os
import re
import sys
import shutil
from pathlib import Path

class SpacetricRebrander:
    
    def __init__(self):
        self.brand_replacements = {
            # Brand Name Variations
            'Gadgetronix': 'Spacetric',
            'GADGETRONIX': 'SPACETRIC',  
            'gadgetronix': 'spacetric',
            'GadgetroniX': 'Spacetric',
            'Gadgetronix.Net': 'Spacetric',
            'GX': 'ST',  # Logo abbreviations
            
            # Taglines and Slogans
            'Re-invent How You Power Your Life': 'Transforming Technology Solutions',
            'Tanzania\'s top provider': 'Tanzania\'s innovative leader',
            'sustainable energy, security systems, and telecom solutions': 
                'advanced energy systems, water solutions, security, and telecommunications',
            
            # Domain and URLs
            'gadgetronix.net': 'spacetric.co.tz',
            'https://gadgetronix.net': 'https://spacetric.co.tz',
            'www.gadgetronix.net': 'www.spacetric.co.tz',
            
            # Email Addresses
            'sales@gadgetronix.net': 'sales@spacetric.co.tz',
            'info@gadgetronix.net': 'info@spacetric.co.tz',
            'support@gadgetronix.net': 'support@spacetric.co.tz',
            
            # Content Paraphrasing Templates
            'We provide comprehensive solutions': 'We deliver integrated technology solutions',
            'suppliers, consultants, designers, and project implementers': 
                'solution providers, consultants, engineers, and implementation specialists',
            'greater value to our customers': 'exceptional value to our clients',
            'quality of our services is unrivaled': 'service excellence is unmatched',
            'passion for technological innovation': 'commitment to innovative technology',
            
            # Business Descriptions  
            'energy, security systems, and telecom solutions': 
                'energy systems, water treatment, security, and telecommunications',
            'residential and commercial needs': 'residential, commercial, and industrial applications',
            'sustainable energy solutions': 'advanced energy and infrastructure solutions',
        }
        
        self.meta_tag_updates = {
            'content="Gadgetronix"': 'content="Spacetric"',
            'name="Gadgetronix"': 'name="Spacetric"',
            'alt="Gadgetronix"': 'alt="Spacetric"',
            'title="Gadgetronix"': 'title="Spacetric"',
        }
        
        # Files to process
        self.html_extensions = ['.html', '.htm']
        self.css_extensions = ['.css']
        self.js_extensions = ['.js']
        
    def process_file(self, file_path):
        """Process a single file for rebranding"""
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()
            
            # Apply brand replacements
            modified_content = content
            for old_text, new_text in self.brand_replacements.items():
                modified_content = modified_content.replace(old_text, new_text)
            
            # Apply meta tag updates
            for old_meta, new_meta in self.meta_tag_updates.items():
                modified_content = modified_content.replace(old_meta, new_meta)
            
            # Special handling for structured data and JSON-LD
            modified_content = self.update_structured_data(modified_content)
            
            # Update social media links
            modified_content = self.update_social_links(modified_content)
            
            return modified_content
            
        except Exception as e:
            print(f"Error processing file {file_path}: {str(e)}")
            return None
    
    def update_structured_data(self, content):
        """Update JSON-LD structured data"""
        # Update organization schema
        content = re.sub(
            r'"@id":"https://gadgetronix\.net/#organization"',
            '"@id":"https://spacetric.co.tz/#organization"',
            content
        )
        
        # Update website schema
        content = re.sub(
            r'"@id":"https://gadgetronix\.net/#website"',
            '"@id":"https://spacetric.co.tz/#website"',
            content
        )
        
        return content
    
    def update_social_links(self, content):
        """Update social media sharing links"""
        # Twitter/X sharing
        content = re.sub(
            r'https://twitter\.com/share\?text=([^&]+)&amp;url=https%3A%2F%2Fgadgetronix\.net',
            r'https://twitter.com/share?text=\1&amp;url=https%3A%2F%2Fspacetric.co.tz',
            content
        )
        
        # Facebook sharing
        content = re.sub(
            r'https://www\.facebook\.com/sharer/sharer\.php\?u=https%3A%2F%2Fgadgetronix\.net',
            'https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fspacetric.co.tz',
            content
        )
        
        # LinkedIn sharing
        content = re.sub(
            r'https://www\.linkedin\.com/shareArticle\?[^"]*gadgetronix\.net[^"]*',
            lambda m: m.group(0).replace('gadgetronix.net', 'spacetric.co.tz'),
            content
        )
        
        return content
    
    def process_directory(self, source_dir, output_dir):
        """Process all files in a directory"""
        source_path = Path(source_dir)
        output_path = Path(output_dir)
        
        # Create output directory if it doesn't exist
        output_path.mkdir(parents=True, exist_ok=True)
        
        processed_count = 0
        error_count = 0
        
        for file_path in source_path.rglob('*'):
            if file_path.is_file():
                relative_path = file_path.relative_to(source_path)
                output_file_path = output_path / relative_path
                
                # Create directory structure
                output_file_path.parent.mkdir(parents=True, exist_ok=True)
                
                # Process text files
                if file_path.suffix.lower() in (self.html_extensions + self.css_extensions + self.js_extensions):
                    modified_content = self.process_file(file_path)
                    
                    if modified_content is not None:
                        try:
                            with open(output_file_path, 'w', encoding='utf-8') as output_file:
                                output_file.write(modified_content)
                            processed_count += 1
                            print(f"✅ Processed: {relative_path}")
                        except Exception as e:
                            print(f"❌ Error writing {relative_path}: {str(e)}")
                            error_count += 1
                    else:
                        error_count += 1
                
                # Copy binary files (images, etc.)
                else:
                    try:
                        shutil.copy2(file_path, output_file_path)
                        print(f"📁 Copied: {relative_path}")
                    except Exception as e:
                        print(f"❌ Error copying {relative_path}: {str(e)}")
                        error_count += 1
        
        return processed_count, error_count
    
    def generate_summary_report(self, processed_count, error_count, output_dir):
        """Generate a summary report of the rebrand process"""
        report_content = f"""
# SPACETRIC REBRAND COMPLETION REPORT

## Summary
- **Files Processed**: {processed_count}
- **Errors Encountered**: {error_count}
- **Success Rate**: {(processed_count/(processed_count+error_count)*100):.1f}%

## Brand Changes Applied
"""
        
        for old_brand, new_brand in list(self.brand_replacements.items())[:10]:
            report_content += f"- `{old_brand}` → `{new_brand}`\n"
        
        report_content += f"""

## File Locations
- **Output Directory**: {output_dir}
- **Original Files**: Preserved in source location
- **Modified Files**: Available in output directory

## Next Steps
1. Review the rebranded files
2. Test all page functionality  
3. Update any remaining manual content
4. Deploy to production environment

## Manual Review Required
- Double-check contact information
- Verify image alt text descriptions
- Review meta descriptions for SEO
- Test all internal and external links
- Validate structured data markup

Generated: {os.popen('date').read().strip()}
"""
        
        # Write report
        report_path = Path(output_dir) / 'REBRAND_COMPLETION_REPORT.md'
        with open(report_path, 'w') as report_file:
            report_file.write(report_content)
        
        print(f"\n📊 Report generated: {report_path}")

def main():
    """Main execution function"""
    
    # Get command line arguments
    if len(sys.argv) != 3:
        print("Usage: python rebrand-script.py [source_directory] [output_directory]")
        print("Example: python rebrand-script.py /app/gadgetronix.net /app/spacetric-website-complete")
        sys.exit(1)
    
    source_dir = sys.argv[1]
    output_dir = sys.argv[2]
    
    # Validate source directory
    if not os.path.exists(source_dir):
        print(f"❌ Source directory does not exist: {source_dir}")
        sys.exit(1)
    
    print("🚀 SPACETRIC REBRAND AUTOMATION")
    print("=" * 40)
    print(f"Source: {source_dir}")
    print(f"Output: {output_dir}")
    print("=" * 40)
    
    # Initialize rebrander
    rebrander = SpacetricRebrander()
    
    # Process files
    print("\n📁 Processing files...")
    processed_count, error_count = rebrander.process_directory(source_dir, output_dir)
    
    # Generate report
    print(f"\n📊 Generating completion report...")
    rebrander.generate_summary_report(processed_count, error_count, output_dir)
    
    print(f"\n✅ REBRAND COMPLETE!")
    print(f"📁 Rebranded website available at: {output_dir}")
    print(f"📊 Files processed: {processed_count}")
    print(f"❌ Errors: {error_count}")

if __name__ == "__main__":
    main()

# ADDITIONAL UTILITY FUNCTIONS

def quick_rebrand_sample():
    """Quick rebrand of a sample file for testing"""
    sample_content = """
    <title>GADGETRONIX | Re-invent How You Power Your Life</title>
    <meta name="description" content="Tanzania's top provider of sustainable energy, security systems, and telecom solutions"/>
    <h1>Welcome to Gadgetronix</h1>
    <p>We provide comprehensive solutions for everyone as suppliers, consultants, designers, and project implementers.</p>
    <a href="https://gadgetronix.net/contact">Contact sales@gadgetronix.net</a>
    """
    
    rebrander = SpacetricRebrander()
    
    # Apply replacements
    result = sample_content
    for old_text, new_text in rebrander.brand_replacements.items():
        result = result.replace(old_text, new_text)
    
    print("BEFORE:")
    print(sample_content)
    print("\nAFTER:")
    print(result)

# Run sample if called with --test flag
if len(sys.argv) > 1 and sys.argv[1] == '--test':
    quick_rebrand_sample()